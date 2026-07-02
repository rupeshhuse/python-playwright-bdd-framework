"""Playwright-specific defaults and helpers for the automation framework."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Final

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent
REPORTS_DIR: Final[Path] = PROJECT_ROOT / "reports"
SCREENSHOTS_DIR: Final[Path] = PROJECT_ROOT / "screenshots"
LOGS_DIR: Final[Path] = PROJECT_ROOT / "logs"

BROWSER_NAMES: Final[tuple[str, ...]] = ("chromium", "firefox", "webkit")
DEFAULT_BROWSER: Final[str] = os.getenv("PLAYWRIGHT_BROWSER", "chromium")
DEFAULT_HEADLESS: Final[bool] = os.getenv("HEADLESS", "true").lower() == "true"
DEFAULT_TIMEOUT: Final[int] = int(os.getenv("DEFAULT_TIMEOUT", "15000"))
DEFAULT_BASE_URL: Final[str] = os.getenv("BASE_URL", "https://www.saucedemo.com")


def ensure_directories() -> None:
    """Create output directories used by Playwright and reporting."""
    for directory in (REPORTS_DIR, SCREENSHOTS_DIR, LOGS_DIR):
        directory.mkdir(parents=True, exist_ok=True)


ensure_directories()
