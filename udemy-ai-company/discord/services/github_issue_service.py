from __future__ import annotations

import requests
from typing import Any


class GitHubIssueService:
    def __init__(self, token: str, repo: str) -> None:
        self.repo = repo
        self.base_url = f"https://api.github.com/repos/{repo}"
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "udemy-ai-company-discord-command-center",
            }
        )

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        response = self.session.request(method, f"{self.base_url}{path}", timeout=30, **kwargs)
        if not response.ok:
            raise RuntimeError(f"GitHub API {method} {path} failed: {response.status_code} {response.text}")
        if response.status_code == 204:
            return None
        return response.json()

    def create_issue(self, title: str, body: str, labels: list[str]) -> dict[str, Any]:
        payload = {"title": title, "body": body, "labels": labels}
        try:
            return self.request("POST", "/issues", json=payload)
        except RuntimeError:
            payload["labels"] = []
            issue = self.request("POST", "/issues", json=payload)
            self.comment_issue(
                issue["number"],
                "Discord Command Center: ラベル付き作成に失敗したため、Issueのみ作成しました。"
                "`scripts/create_github_labels.sh` を確認してください。",
            )
            return issue

    def get_issue(self, issue_number: int) -> dict[str, Any]:
        return self.request("GET", f"/issues/{issue_number}")

    def list_issues(self, state: str = "open", labels: list[str] | None = None, limit: int = 10) -> list[dict[str, Any]]:
        params: dict[str, Any] = {"state": state, "per_page": min(limit, 100), "sort": "updated", "direction": "desc"}
        if labels:
            params["labels"] = ",".join(labels)
        issues = self.request("GET", "/issues", params=params)
        return [issue for issue in issues if "pull_request" not in issue]

    def comment_issue(self, issue_number: int, body: str) -> dict[str, Any]:
        return self.request("POST", f"/issues/{issue_number}/comments", json={"body": body})

    def add_labels(self, issue_number: int, labels: list[str]) -> None:
        if labels:
            self.request("POST", f"/issues/{issue_number}/labels", json={"labels": labels})


def label_names(issue: dict[str, Any]) -> list[str]:
    return [label["name"] for label in issue.get("labels", []) if label.get("name")]
