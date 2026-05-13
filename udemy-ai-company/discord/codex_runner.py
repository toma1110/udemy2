from __future__ import annotations

import subprocess
import shlex
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path


@dataclass(frozen=True)
class CodexRunResult:
    issue_number: int
    exit_code: int
    log_path: Path
    stdout_tail: str
    stderr_tail: str
    started_at: str
    completed_at: str


class CodexRunner:
    def __init__(self, command: str, timeout_seconds: int, log_dir: Path) -> None:
        self.command = command
        self.timeout_seconds = timeout_seconds
        self.log_dir = log_dir

    def run(self, issue_number: int, prompt: str, workspace: Path) -> CodexRunResult:
        self.log_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now(UTC).strftime("%Y%m%d%H%M%S")
        log_path = self.log_dir / f"issue-{issue_number}-{timestamp}.log"
        started_at = datetime.now(UTC).isoformat()

        try:
            result = subprocess.run(
                shlex.split(self.command),
                input=prompt,
                text=True,
                capture_output=True,
                cwd=workspace,
                timeout=self.timeout_seconds,
                check=False,
            )
            exit_code = result.returncode
            stdout = result.stdout
            stderr = result.stderr
        except subprocess.TimeoutExpired as exc:
            exit_code = 124
            stdout = exc.stdout or ""
            stderr = (exc.stderr or "") + f"\nTimed out after {self.timeout_seconds} seconds."

        completed_at = datetime.now(UTC).isoformat()
        log_path.write_text(
            "\n".join(
                [
                    f"$ {self.command}",
                    f"workspace: {workspace}",
                    f"started_at: {started_at}",
                    f"completed_at: {completed_at}",
                    f"exit_code: {exit_code}",
                    "",
                    "[prompt]",
                    prompt,
                    "",
                    "[stdout]",
                    stdout,
                    "",
                    "[stderr]",
                    stderr,
                    "",
                ]
            ),
            encoding="utf-8",
        )
        return CodexRunResult(
            issue_number=issue_number,
            exit_code=exit_code,
            log_path=log_path,
            stdout_tail=tail(stdout),
            stderr_tail=tail(stderr),
            started_at=started_at,
            completed_at=completed_at,
        )


def tail(text: str, limit: int = 3000) -> str:
    stripped = text.strip()
    if len(stripped) <= limit:
        return stripped
    return stripped[-limit:]
