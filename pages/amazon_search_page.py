"""Page object for the Google search to Amazon India journey."""
from __future__ import annotations

import re

from base_page import BasePage
from locators.amazon_search_locators import AmazonSearchLocators


class AmazonSearchPage(BasePage):
    """Encapsulates interactions for the Google search and Amazon navigation flow."""

    def __init__(self, page) -> None:
        super().__init__(page)

    def search_google(self, query: str) -> None:
        """Search the requested term on Google."""
        self.fill(AmazonSearchLocators.GOOGLE_SEARCH_BOX, query)
        self.press_key("Enter")
        self.wait_for_page_load()

    def click_official_result(self) -> None:
        """Open the official Amazon India result from the Google search page."""
        result_locator = self.page.get_by_role(
            "link",
            name=re.compile(r"Online Shopping site in India", re.IGNORECASE),
        ).first
        result_locator.wait_for(timeout=15000)
        result_locator.click()
        self.wait_for_page_load()
