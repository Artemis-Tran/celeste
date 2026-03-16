from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    google_service_account_file: str
    google_sheet_id: str
    google_worksheet_name: str = "applications"

    @classmethod
    def from_env(cls) -> "Settings":
        service_account_file = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE", "").strip()
        sheet_id = os.getenv("GOOGLE_SHEET_ID", "").strip()
        worksheet_name = os.getenv("GOOGLE_WORKSHEET_NAME", "applications").strip()

        missing = [
            name
            for name, value in (
                ("GOOGLE_SERVICE_ACCOUNT_FILE", service_account_file),
                ("GOOGLE_SHEET_ID", sheet_id),
            )
            if not value
        ]
        if missing:
            missing_fields = ", ".join(missing)
            raise ValueError(f"Missing required environment variables: {missing_fields}")

        return cls(
            google_service_account_file=service_account_file,
            google_sheet_id=sheet_id,
            google_worksheet_name=worksheet_name or "applications",
        )
