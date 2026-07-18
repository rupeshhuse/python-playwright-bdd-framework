"""Page object for validating Amazon India upper navigation links."""
from __future__ import annotations

from typing import Any

from base_page import BasePage


class InternalLinksPage(BasePage):
    """Encapsulates interactions with the Amazon India top navigation grid."""

    NAV_LINKS_SELECTOR = "#nav-xshop a"

    def __init__(self, page) -> None:
        super().__init__(page)

    def open_homepage(self) -> None:
        """Open the Amazon India homepage and wait for it to finish loading."""
        self.page.goto("https://www.amazon.in/", wait_until="domcontentloaded", timeout=30000)
        self.wait_for_page_load()

    def collect_visible_navigation_links(self) -> list[dict[str, Any]]:
        """Return the visible navigation links from the upper Amazon grid."""
        links: list[dict[str, Any]] = []
        count = self.page.locator(self.NAV_LINKS_SELECTOR).count()

        for index in range(count):
            locator = self.page.locator(self.NAV_LINKS_SELECTOR).nth(index)
            if not locator.is_visible():
                continue

            text = locator.inner_text().strip().replace("\n", " ").replace("\t", " ")
            href = locator.get_attribute("href") or ""
            if not href or href.startswith("javascript"):
                continue

            links.append({
                "index": index,
                "text": " ".join(text.split()),
                "href": href,
            })

        return links[:12]

    def validate_link(self, link: dict[str, Any]) -> dict[str, Any]:
        """Navigate to the given link and verify the destination is valid."""
        self.open_homepage()

        locator = self.page.locator(self.NAV_LINKS_SELECTOR).nth(link["index"])
        locator.scroll_into_view_if_needed()
        locator.click()
        self.page.wait_for_timeout(1000)

        current_url = self.page.url
        title = self.page.title()
        is_valid = "amazon.in" in current_url.lower() or "amazon.com" in current_url.lower()
        return {
            "text": link["text"],
            "href": link["href"],
            "current_url": current_url,
            "title": title,
            "is_valid": is_valid,
        }
