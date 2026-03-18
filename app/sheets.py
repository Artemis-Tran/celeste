from __future__ import annotations

import gspread
from google.oauth2.service_account import Credentials

from app.config import Settings


GOOGLE_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]


class GoogleSheetsClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def get_worksheet(self) -> gspread.Worksheet:
        spreadsheet = self._get_client().open_by_key(self.settings.google_sheet_id)
        return spreadsheet.worksheet(self.settings.google_worksheet_name)

    def _get_client(self) -> gspread.Client:
        credentials = Credentials.from_service_account_file(
            self.settings.google_service_account_file,
            scopes=GOOGLE_SCOPES,
        )
        return gspread.authorize(credentials)
