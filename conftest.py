"""Pytest hooks and fixtures for non-Behave test execution.

This module provides the reusable fixture used by pytest-based UI tests.
"""
from __future__ import annotations

import pytest
from playwright.sync_api import Page

from browser_manager import BrowserManager
from config_reader import ConfigReader
from logger import get_logger

LOGGER = get_logger("pytest")


@pytest.fixture(scope="function")
def browser_page() -> Page:
    """Create a browser page for pytest-based UI tests."""
    config_reader = ConfigReader()
    browser_manager = BrowserManager(config_reader=config_reader)
    page = browser_manager.launch(browser_name="chromium", headless=True)
    yield page
    browser_manager.close()
    LOGGER.info("Pytest browser fixture completed")
