"""Browser lifecycle management for Playwright.

This module owns browser launch, context setup, screenshot capture, and cleanup so
page objects and hooks do not need to manage Playwright directly.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from constants import DEFAULT_BROWSER, DEFAULT_HEADLESS, DEFAULT_TIMEOUT, SCREENSHOTS_DIR
from logger import get_logger

LOGGER = get_logger("browser_manager")


class BrowserManager:
    """Owns Playwright browser launch and teardown."""

    def __init__(self, config_reader: Any | None = None) -> None:
        self.config_reader = config_reader
        self.playwright = None
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None
        self.page: Page | None = None
        self._closed = False

    def launch(self, browser_name: str = DEFAULT_BROWSER, headless: bool = DEFAULT_HEADLESS) -> Page:
        """Launch a browser instance using the requested settings."""
        if self._closed:
            self._closed = False
        self.playwright = sync_playwright().start()
        browser_type = getattr(self.playwright, browser_name, None)
        if browser_type is None:
            raise ValueError(f"Unsupported browser: {browser_name}")
        self.browser = browser_type.launch(headless=headless)
        self.context = self.browser.new_context(viewport={"width": 1440, "height": 900})
        self.page = self.context.new_page()
        self.page.set_default_timeout(DEFAULT_TIMEOUT)
        LOGGER.info("Launched %s browser in %s mode", browser_name, "headless" if headless else "headed")
        return self.page

    def take_screenshot(self, name: str) -> Path:
        """Capture a failure screenshot and return its path."""
        if self.page is None:
            raise RuntimeError("Page is not initialized")
        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        screenshot_path = SCREENSHOTS_DIR / f"{name.replace(' ', '_').lower()}_failure.png"
        self.page.screenshot(path=str(screenshot_path), full_page=True)
        LOGGER.info("Failure screenshot saved: %s", screenshot_path)
        return screenshot_path

    def close(self) -> None:
        """Ensure the browser and Playwright context are closed once."""
        if self._closed:
            return

        try:
            if self.context:
                self.context.close()
        except Exception as exc:  # pragma: no cover - defensive cleanup
            LOGGER.warning("Browser context close raised an exception: %s", exc)
        finally:
            self.context = None

        try:
            if self.browser:
                self.browser.close()
        except Exception as exc:  # pragma: no cover - defensive cleanup
            LOGGER.warning("Browser close raised an exception: %s", exc)
        finally:
            self.browser = None
            self.page = None

        try:
            if self.playwright:
                self.playwright.stop()
        except Exception as exc:  # pragma: no cover - defensive cleanup
            LOGGER.warning("Playwright stop raised an exception: %s", exc)
        finally:
            self.playwright = None
            self._closed = True
