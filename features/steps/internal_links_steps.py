"""Behave step definitions for validating Amazon India upper navigation links."""
from __future__ import annotations

from behave import given, then, when

from pages.internal_links_page import InternalLinksPage


@given("the user opens the Amazon India homepage")
def step_open_amazon_homepage(context) -> None:
    """Open Amazon India and create the page object for link validation."""
    context.internal_links_page = InternalLinksPage(context.page)
    context.internal_links_page.open_homepage()


@when("the user collects the visible upper navigation links")
def step_collect_upper_navigation_links(context) -> None:
    """Collect the visible links from the Amazon India upper navigation grid."""
    context.navigation_links = context.internal_links_page.collect_visible_navigation_links()


@then("each visible link with a valid destination should be clickable")
def step_validate_links_are_clickable(context) -> None:
    """Ensure each collected link can be identified and is clickable."""
    assert context.navigation_links, "No visible upper navigation links were found"
    for link in context.navigation_links:
        assert link.get("href"), f"Link {link.get('text')} has no destination"
        assert not link.get("href", "").startswith("javascript"), f"Link {link.get('text')} is not a real destination"


@then("each clicked link should navigate to a valid Amazon destination")
def step_validate_each_clicked_link(context) -> None:
    """Open each link and verify it lands on a valid Amazon destination."""
    results = []
    for link in context.navigation_links:
        result = context.internal_links_page.validate_link(link)
        results.append(result)
        assert result["is_valid"], f"Link {result['text']} navigated to an invalid destination: {result['current_url']}"

    context.navigation_results = results


@then("a screenshot should be captured for the navigation validation")
def step_capture_navigation_screenshot(context) -> None:
    """Capture a screenshot after the link validation flow completes."""
    context.internal_links_page.take_screenshot("amazon_navigation_validation")
