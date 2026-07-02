"""Reusable support helpers for data handling and waits."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from playwright.sync_api import Page

from constants import PROJECT_ROOT


def load_json(path: str | Path) -> dict[str, Any]:
    """Load JSON content from a file."""
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def create_test_data_payload(**kwargs: Any) -> dict[str, Any]:
    """Build a simple payload dict for test data reuse."""
    return kwargs


def get_fixture_path(filename: str) -> Path:
    """Return the absolute path to a fixture file under the testdata folder."""
    return PROJECT_ROOT / "testdata" / filename


def wait_for_url(page: Page, expected_url: str, timeout: int = 15000) -> None:
    """Wait until the page URL contains the expected fragment."""
    page.wait_for_url(f"**/{expected_url}", timeout=timeout)
