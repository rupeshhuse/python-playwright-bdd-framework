"""Shared Behave hooks used by both project-level and feature-level hook modules.

This centralizes browser lifecycle management so both entrypoints stay thin and
consistent.
"""
from __future__ import annotations

from typing import Any

from browser_manager import BrowserManager
from config_reader import ConfigReader
from logger import get_logger

LOGGER = get_logger("behave")


def before_all(context: Any) -> None:
    """Initialize shared configuration once before the whole run."""
    context.config_reader = ConfigReader()
    context.logger = LOGGER
    context.browser_manager = BrowserManager(config_reader=context.config_reader)


def before_scenario(context: Any, scenario: Any) -> None:
    """Open a fresh browser page per scenario and attach the page to context."""
    browser_name = context.config.userdata.get("browser", "chromium")
    headless = context.config.userdata.get("headless", "true").lower() == "true"
    context.browser_manager.launch(browser_name=browser_name, headless=headless)
    context.page = context.browser_manager.page
    context.browser = context.browser_manager.browser


def after_scenario(context: Any, scenario: Any) -> None:
    """Close the browser and capture a screenshot when the scenario fails."""
    if getattr(scenario, "status", None) == "failed" and getattr(context, "page", None) is not None:
        context.browser_manager.take_screenshot(scenario.name)
    context.browser_manager.close()


def after_all(context: Any) -> None:
    """Perform cleanup after the full execution."""
    context.browser_manager.close()
