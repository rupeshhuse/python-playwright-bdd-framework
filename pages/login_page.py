"""Page object for the login page."""
from __future__ import annotations

from base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    """Encapsulates interactions with the SauceDemo login page."""

    def __init__(self, page) -> None:
        super().__init__(page)

    def login(self, username: str, password: str) -> None:
        """Fill in the login form and submit it."""
        self.fill(LoginLocators.USERNAME_INPUT, username)
        self.fill(LoginLocators.PASSWORD_INPUT, password)

    def submit_login(self) -> None:
        """Click the login button and wait for page transition."""
        self.click(LoginLocators.LOGIN_BUTTON)
        self.wait_for_page_load()
