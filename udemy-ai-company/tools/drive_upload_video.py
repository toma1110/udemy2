#!/usr/bin/env python3
"""Upload a video file to the configured Google Drive folder."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def get_drive_service() -> Any:
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
            scopes=["https://www.googleapis.com/auth/drive"],
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


def ensure_anyone_reader(service: Any, file_id: str) -> None:
    service.permissions().create(
        fileId=file_id,
        body={"type": "anyone", "role": "reader"},
        fields="id",
        supportsAllDrives=True,
    ).execute()


def upload_video(service: Any, path: Path, folder_id: str, name: str) -> dict[str, Any]:
    from googleapiclient.http import MediaFileUpload

    media = MediaFileUpload(str(path), mimetype="video/mp4", resumable=True)
    metadata: dict[str, Any] = {"name": name, "mimeType": "video/mp4"}
    if folder_id:
        metadata["parents"] = [folder_id]

    created = (
        service.files()
        .create(
            body=metadata,
            media_body=media,
            fields="id,name,size,webViewLink,trashed,parents",
            supportsAllDrives=True,
        )
        .execute()
    )
    ensure_anyone_reader(service, created["id"])
    return (
        service.files()
        .get(
            fileId=created["id"],
            fields="id,name,size,webViewLink,trashed,parents,permissions(type,role)",
            supportsAllDrives=True,
        )
        .execute()
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("--name")
    parser.add_argument("--folder-id", default="")
    parser.add_argument("--env-file", type=Path, default=Path(".env"))
    parser.add_argument("--metadata-output", type=Path)
    args = parser.parse_args()

    load_dotenv(args.env_file)
    folder_id = args.folder_id or os.environ.get("GOOGLE_DRIVE_FOLDER_ID", "")
    if not folder_id:
        raise RuntimeError("Google Drive folder ID is not configured")
    if not args.file.exists():
        raise FileNotFoundError(args.file)

    service = get_drive_service()
    metadata = upload_video(service, args.file, folder_id, args.name or args.file.name)
    if args.metadata_output:
        args.metadata_output.parent.mkdir(parents=True, exist_ok=True)
        args.metadata_output.write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(metadata, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
