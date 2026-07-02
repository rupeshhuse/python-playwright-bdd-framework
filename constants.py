"""Shared constants and configuration defaults."""
from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
REPORTS_DIR = PROJECT_ROOT / "reports"
SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"
LOGS_DIR = PROJECT_ROOT / "logs"

DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "15000"))
DEFAULT_BROWSER = os.getenv("PLAYWRIGHT_BROWSER", "chromium")
DEFAULT_HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
