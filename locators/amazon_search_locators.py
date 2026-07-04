"""Locator constants for the Amazon search flow."""
from __future__ import annotations


class AmazonSearchLocators:
    """CSS selectors used by the Amazon search page object."""

    GOOGLE_SEARCH_BOX = "textarea[name='q']"
    AMAZON_RESULT = "h3:has-text('Online Shopping site in India')"
