from __future__ import annotations

from fastapi import FastAPI, HTTPException

from app.config import Settings
from app.sheets import GoogleSheetsClient


app = FastAPI(title="AI Job Application Tracker Assistant")


@app.get("/worksheet/connection")
def check_worksheet_connection() -> dict[str, str]:
    try:
        settings = Settings.from_env()
        worksheet = GoogleSheetsClient(settings).get_worksheet()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return {
        "status": "connected",
        "worksheet": worksheet.title,
    }
