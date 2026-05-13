from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GuardResult:
    workspace: Path
    dangerous_operations: list[str]


class RunGuard:
    """Validates fixed workspace and records dangerous operations.

    Current policy does not block CloudFormation create/update/delete,
    git push, or git merge. The guard detects them for logging only.
    """

    DANGEROUS_PATTERNS = {
        "cloudformation-create": ("create-stack", "cloudformation deploy", "スタック作成"),
        "cloudformation-update": ("update-stack", "cloudformation deploy", "スタック更新"),
        "cloudformation-delete": ("delete-stack", "スタック削除"),
        "git-push": ("git push",),
        "git-merge": ("git merge",),
    }

    def __init__(self, workspace_root: Path, environment: str, allowed_environments: list[str]) -> None:
        if environment not in allowed_environments:
            raise ValueError(f"Unsupported workspace environment: {environment}")
        self.workspace_root = workspace_root.expanduser().resolve()
        self.environment = environment
        self.allowed_environments = allowed_environments

    @property
    def workspace(self) -> Path:
        return (self.workspace_root / self.environment).resolve()

    def validate(self, prompt: str, issue_body: str) -> GuardResult:
        workspace = self.workspace
        expected_parent = self.workspace_root
        if expected_parent not in [workspace, *workspace.parents]:
            raise ValueError(f"Workspace is outside root: {workspace}")
        if not workspace.exists():
            raise FileNotFoundError(f"Workspace does not exist: {workspace}")
        dangerous = self.detect_dangerous_operations(f"{prompt}\n{issue_body}")
        return GuardResult(workspace=workspace, dangerous_operations=dangerous)

    def detect_dangerous_operations(self, text: str) -> list[str]:
        lowered = text.lower()
        detected: list[str] = []
        for name, patterns in self.DANGEROUS_PATTERNS.items():
            if any(pattern.lower() in lowered for pattern in patterns):
                detected.append(name)
        return detected
