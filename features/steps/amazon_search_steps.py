"""Behave step definitions for the Amazon India search flow."""
from __future__ import annotations

from behave import given, then, when

from pages.amazon_search_page import AmazonSearchPage


@given("the user opens Google search")
def step_open_google(context) -> None:
    """Open Google search and initialize the page object."""
    context.page.goto("https://www.google.com")
    context.amazon_page = AmazonSearchPage(context.page)


@when('the user searches for "{query}"')
def step_search_google(context, query: str) -> None:
    """Enter a search term into the Google search box and submit it."""
    context.amazon_page.search_google(query)


@when("the user clicks the official Amazon India result")
def step_click_official_amazon_result(context) -> None:
    """Navigate to the official Amazon India result from Google search."""
    context.amazon_page.click_official_result()


@then("the Amazon India homepage should load")
def step_verify_amazon_homepage(context) -> None:
    """Assert that the Amazon India homepage opened successfully."""
    expected_url = "https://www.amazon.in/"
    assert context.page.url.startswith(expected_url)


@then('the page title should contain "{text}"')
def step_validate_title(context, text: str) -> None:
    """Validate the current page title contains the expected text."""
    assert text.lower() in context.page.title().lower()


@then('the page URL should contain "{text}"')
def step_validate_url(context, text: str) -> None:
    """Validate the current page URL contains the expected text."""
    assert text.lower() in context.page.url.lower()


@then("a screenshot should be captured")
def step_capture_screenshot(context) -> None:
    """Capture a screenshot for the visited page."""
    context.amazon_page.take_screenshot("amazon_india_homepage")
