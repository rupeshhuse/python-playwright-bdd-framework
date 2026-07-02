"""Behave step definitions for the login feature."""
from __future__ import annotations

from behave import given, then, when

from constants import BASE_URL
from helpers import get_fixture_path, load_json
from pages.login_page import LoginPage


@given("the user opens the login page")
def step_open_login_page(context) -> None:
    """Open the application login page using the browser page from the environment hook."""
    context.test_data = load_json(get_fixture_path("login_data.json"))
    target_url = context.config_reader.get("base_url", BASE_URL)
    context.page.goto(target_url)
    context.login_page = LoginPage(context.page)


@when("the user enters valid credentials")
def step_enter_valid_credentials(context) -> None:
    """Fill the username and password fields with valid sample data."""
    context.login_page.login(
        context.test_data["valid_username"],
        context.test_data["valid_password"],
    )


@when("the user clicks the login button")
def step_click_login_button(context) -> None:
    """Submit the login form."""
    context.login_page.submit_login()


@then("the user should be redirected to the inventory page")
def step_verify_inventory_page(context) -> None:
    """Assert that the inventory page is displayed after successful login."""
    assert "inventory" in context.page.url.lower()
