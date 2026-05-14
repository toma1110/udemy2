#!/usr/bin/env python3
"""Trash or inspect explicit Google Drive file IDs for course asset cleanup."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def get_drive_service():
    from googleapiclient.discovery import build

    refresh_token = os.environ.get("GOOGLE_OAUTH_REFRESH_TOKEN")
    client_id = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")

    if refresh_token and client_id and client_secret:
        from google.oauth2.credentials import Credentials

        credentials = Credentials(
            token=None,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret,
        )
        return build("drive", "v3", credentials=credentials)

    service_account_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not service_account_json:
        raise RuntimeError("Google Drive credentials are not configured")

    from google.oauth2.service_account import Credentials as SACredentials

    credentials = SACredentials.from_service_account_info(
        json.loads(service_account_json),
        scopes=["https://www.googleapis.com/auth/drive"],
    )
    return build("drive", "v3", credentials=credentials)


def get_metadata(service, file_id: str) -> dict:
    return (
        service.files()
        .get(
            fileId=file_id,
            fields="id,name,mimeType,size,trashed,webViewLink,modifiedTime",
            supportsAllDrives=True,
        )
        .execute()
    )


def trash_file(service, file_id: str) -> dict:
    before = get_metadata(service, file_id)
    service.files().update(
        fileId=file_id,
        body={"trashed": True},
        fields="id,name,trashed",
        supportsAllDrives=True,
    ).execute()
    after = get_metadata(service, file_id)
    return {"before": before, "after": after}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-file", type=Path, default=Path(".env"))
    parser.add_argument("--mode", choices=["inspect", "trash"], default="inspect")
    parser.add_argument("--file-id", action="append", required=True)
    args = parser.parse_args()

    load_dotenv(args.env_file)
    service = get_drive_service()

    results = []
    for file_id in args.file_id:
        if args.mode == "trash":
            result = trash_file(service, file_id)
        else:
            metadata = get_metadata(service, file_id)
            result = {"before": metadata, "after": metadata}
        results.append(result)

    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
