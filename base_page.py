"""Reusable page-object base class with explicit-wait helpers.

This module centralizes browser interaction methods so page objects stay thin and
consistent across the framework.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from playwright.sync_api import Locator, Page

from constants import DEFAULT_TIMEOUT, SCREENSHOTS_DIR
from logger import get_logger

LOGGER = get_logger("base_page")


class BasePage:
    """Encapsulates common browser interactions using explicit waits only."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def _locator(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> Locator:
        """Return a locator after waiting for the element to be attached."""
        self.wait_for_element(selector, timeout=timeout)
        return self.page.locator(selector)

    def click(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Click a visible and enabled element."""
        self._locator(selector, timeout=timeout).click(timeout=timeout)

    def fill(self, selector: str, value: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Type text into an input field."""
        self._locator(selector, timeout=timeout).fill(value, timeout=timeout)

    def clear(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Clear the contents of an input field."""
        self._locator(selector, timeout=timeout).clear(timeout=timeout)

    def select_dropdown(self, selector: str, value: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Select an option from a dropdown by visible text or value."""
        self._locator(selector, timeout=timeout).select_option(value=value, timeout=timeout)

    def hover(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Hover over an element."""
        self._locator(selector, timeout=timeout).hover(timeout=timeout)

    def double_click(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Double-click an element."""
        self._locator(selector, timeout=timeout).dblclick(timeout=timeout)

    def right_click(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Open the context menu for an element."""
        self._locator(selector, timeout=timeout).click(button="right", timeout=timeout)

    def drag_and_drop(self, source: str, target: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Drag one element and drop it onto another."""
        self.wait_for_element(source, timeout=timeout)
        self.wait_for_element(target, timeout=timeout)
        self.page.locator(source).drag_to(self.page.locator(target))

    def upload_file(self, selector: str, file_path: str | Path, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Upload a file using a file input."""
        self._locator(selector, timeout=timeout).set_input_files(str(file_path), timeout=timeout)

    def download_file(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> Any:
        """Trigger a download and return the resulting download object."""
        self._locator(selector, timeout=timeout)
        with self.page.expect_download() as download_info:
            self._locator(selector, timeout=timeout).click(timeout=timeout)
        return download_info.value

    def wait_for_element(self, selector: str, timeout: int = DEFAULT_TIMEOUT, state: str = "visible") -> None:
        """Wait for a locator to reach the requested state."""
        self.page.locator(selector).wait_for(state=state, timeout=timeout)

    def wait_for_page_load(self, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Wait for the page lifecycle to settle without hanging on every network condition."""
        self.page.wait_for_load_state("domcontentloaded", timeout=timeout)
        self.page.wait_for_load_state("load", timeout=timeout)
        try:
            self.page.wait_for_load_state("networkidle", timeout=timeout)
        except Exception:  # pragma: no cover - defensive wait handling
            LOGGER.debug("Network idle wait timed out; continuing execution")

    def scroll_into_view(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Scroll the target element into view."""
        self._locator(selector, timeout=timeout).scroll_into_view_if_needed(timeout=timeout)

    def scroll_to_bottom(self) -> None:
        """Scroll to the bottom of the page."""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def press_key(self, key: str) -> None:
        """Press a single keyboard key."""
        self.page.keyboard.press(key)

    def take_screenshot(self, name: str) -> Path:
        """Capture a screenshot and save it under the screenshots folder."""
        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        safe_name = "_".join(part for part in name.lower().split() if part)
        screenshot_path = SCREENSHOTS_DIR / f"{safe_name}_{self.page.title()[:20] or 'page'}.png"
        self.page.screenshot(path=str(screenshot_path), full_page=True)
        LOGGER.info("Screenshot saved: %s", screenshot_path)
        return screenshot_path

    def get_text(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> str:
        """Retrieve visible text from an element."""
        return self._locator(selector, timeout=timeout).inner_text()

    def get_attribute(self, selector: str, attribute: str, timeout: int = DEFAULT_TIMEOUT) -> str | None:
        """Retrieve an attribute value from an element."""
        return self._locator(selector, timeout=timeout).get_attribute(attribute)

    def is_visible(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> bool:
        """Return True when an element is visible."""
        self.wait_for_element(selector, timeout=timeout)
        return self.page.locator(selector).is_visible()

    def is_enabled(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> bool:
        """Return True when an element is enabled."""
        self.wait_for_element(selector, timeout=timeout)
        return self.page.locator(selector).is_enabled()

    def is_checked(self, selector: str, timeout: int = DEFAULT_TIMEOUT) -> bool:
        """Return True when a checkbox is checked."""
        self.wait_for_element(selector, timeout=timeout)
        return self.page.locator(selector).is_checked()
