"""Simple pytest smoke test that exercises the framework scaffolding."""
from __future__ import annotations

import pytest
from playwright.sync_api import Page

from constants import BASE_URL


@pytest.mark.smoke
def test_placeholder(browser_page: Page) -> None:
    """Open the login page and verify that the page title is present."""
    browser_page.goto(BASE_URL)
    assert browser_page.title()
    assert "Swag Labs" in browser_page.title()
