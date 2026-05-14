from __future__ import annotations

import logging
import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

import pymysql
from flask import Flask, redirect, render_template_string, request, url_for


APP_DIR = Path(__file__).resolve().parent
LOG_PATH = APP_DIR / "app.log"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("sre-todo-app")

app = Flask(__name__)


def xray_enabled() -> bool:
    return os.getenv("XRAY_ENABLED", "true").lower() in {"1", "true", "yes", "on"}


if xray_enabled():
    try:
        from aws_xray_sdk.core import xray_recorder
        from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

        xray_recorder.configure(service="sre-todo-app")
        XRayMiddleware(app, xray_recorder)
        logger.info("xray middleware enabled")
    except Exception as exc:  # X-Ray daemonなしのローカル起動でも落とさない
        logger.warning("xray middleware skipped: %s", exc)


def use_mysql() -> bool:
    return bool(os.getenv("DB_HOST"))


@contextmanager
def db_connection() -> Iterator[pymysql.connections.Connection | sqlite3.Connection]:
    if use_mysql():
        conn = pymysql.connect(
            host=os.environ["DB_HOST"],
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER", "admin"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "sreapp"),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False,
        )
    else:
        conn = sqlite3.connect(APP_DIR / "todos.sqlite3")
        conn.row_factory = sqlite3.Row

    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db() -> None:
    with db_connection() as conn:
        if use_mysql():
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS todos (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      title VARCHAR(255) NOT NULL,
                      completed BOOLEAN NOT NULL DEFAULT FALSE,
                      created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
                    """
                )
        else:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS todos (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  completed INTEGER NOT NULL DEFAULT 0,
                  created_at TEXT NOT NULL
                )
                """
            )


def fetch_todos() -> list[dict]:
    with db_connection() as conn:
        if use_mysql():
            with conn.cursor() as cur:
                cur.execute("SELECT id, title, completed, created_at FROM todos ORDER BY id DESC")
                rows = cur.fetchall()
        else:
            rows = conn.execute("SELECT id, title, completed, created_at FROM todos ORDER BY id DESC").fetchall()
            rows = [dict(row) for row in rows]
    return rows


def add_todo(title: str) -> None:
    created_at = datetime.now(timezone.utc).isoformat()
    with db_connection() as conn:
        if use_mysql():
            with conn.cursor() as cur:
                cur.execute("INSERT INTO todos (title) VALUES (%s)", (title,))
        else:
            conn.execute("INSERT INTO todos (title, created_at) VALUES (?, ?)", (title, created_at))
    logger.info("todo created title=%s", title)


def set_todo_completed(todo_id: int, completed: bool) -> None:
    with db_connection() as conn:
        if use_mysql():
            with conn.cursor() as cur:
                cur.execute("UPDATE todos SET completed=%s WHERE id=%s", (completed, todo_id))
        else:
            conn.execute("UPDATE todos SET completed=? WHERE id=?", (1 if completed else 0, todo_id))
    logger.info("todo updated id=%s completed=%s", todo_id, completed)


def delete_todo(todo_id: int) -> None:
    with db_connection() as conn:
        if use_mysql():
            with conn.cursor() as cur:
                cur.execute("DELETE FROM todos WHERE id=%s", (todo_id,))
        else:
            conn.execute("DELETE FROM todos WHERE id=?", (todo_id,))
    logger.info("todo deleted id=%s", todo_id)


PAGE = """
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>SRE TODO App</title>
    <style>
      body { font-family: system-ui, sans-serif; margin: 0; background: #f5f7fb; color: #17202a; }
      main { max-width: 760px; margin: 48px auto; padding: 0 20px; }
      h1 { margin-bottom: 8px; }
      .meta { color: #5f6b7a; margin-bottom: 24px; }
      form.add { display: flex; gap: 8px; margin-bottom: 20px; }
      input[type=text] { flex: 1; padding: 12px; border: 1px solid #ccd3dd; border-radius: 8px; }
      button { padding: 10px 14px; border: 0; border-radius: 8px; background: #ff9900; color: #16191f; font-weight: 700; cursor: pointer; }
      ul { list-style: none; padding: 0; display: grid; gap: 10px; }
      li { background: #fff; border: 1px solid #d9e0ea; border-radius: 8px; padding: 12px; display: flex; align-items: center; gap: 10px; }
      .done { color: #64748b; text-decoration: line-through; }
      .spacer { flex: 1; }
      .danger { background: #e5484d; color: #fff; }
    </style>
  </head>
  <body>
    <main>
      <h1>SRE TODO App</h1>
      <div class="meta">Backend: {{ backend }} / Log: app.log / Health: /health</div>
      <form class="add" method="post" action="{{ url_for('create') }}">
        <input type="text" name="title" placeholder="TODOを入力" required maxlength="255">
        <button type="submit">追加</button>
      </form>
      <ul>
        {% for todo in todos %}
          <li>
            <form method="post" action="{{ url_for('toggle', todo_id=todo.id) }}">
              <input type="hidden" name="completed" value="{{ 0 if todo.completed else 1 }}">
              <button type="submit">{{ "戻す" if todo.completed else "完了" }}</button>
            </form>
            <span class="{{ 'done' if todo.completed else '' }}">{{ todo.title }}</span>
            <span class="spacer"></span>
            <form method="post" action="{{ url_for('remove', todo_id=todo.id) }}">
              <button class="danger" type="submit">削除</button>
            </form>
          </li>
        {% else %}
          <li>まだTODOはありません。</li>
        {% endfor %}
      </ul>
    </main>
  </body>
</html>
"""


@app.before_request
def log_request() -> None:
    logger.info("request method=%s path=%s remote_addr=%s", request.method, request.path, request.remote_addr)


@app.get("/")
def index():
    init_db()
    return render_template_string(PAGE, todos=fetch_todos(), backend="MySQL" if use_mysql() else "SQLite")


@app.post("/todos")
def create():
    title = request.form.get("title", "").strip()
    if title:
        add_todo(title)
    return redirect(url_for("index"))


@app.post("/todos/<int:todo_id>/toggle")
def toggle(todo_id: int):
    completed = request.form.get("completed") == "1"
    set_todo_completed(todo_id, completed)
    return redirect(url_for("index"))


@app.post("/todos/<int:todo_id>/delete")
def remove(todo_id: int):
    delete_todo(todo_id)
    return redirect(url_for("index"))


@app.get("/health")
def health():
    try:
        init_db()
        return {"status": "ok", "database": "mysql" if use_mysql() else "sqlite"}
    except Exception as exc:
        logger.exception("health check failed")
        return {"status": "error", "message": str(exc)}, 500


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.getenv("APP_PORT", "5000")))

