from functools import cached_property

from selenium.common.exceptions import TimeoutException

from framework.base_page import BasePage
from framework.constants.credentials import CREDENTIALS
from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper
from framework.utils.web_element_wrapper import WebElementWrapper


class LoginPage(BasePage):
    class Locators:
        USERNAME_INPUT = Locator.name("username")
        PASSWORD_INPUT = Locator.name("password")
        LOGIN_BUTTON = Locator.css("div.login input.button[value='Log In']")
        ERROR_TITLE = Locator.class_name("title")

    def __init__(self, driver: WebDriverWrapper):
        super().__init__(driver)

    @cached_property
    def username_input(self):
        return WebElementWrapper(self.driver, self.Locators.USERNAME_INPUT)

    @cached_property
    def password_input(self):
        return WebElementWrapper(self.driver, self.Locators.PASSWORD_INPUT)

    @cached_property
    def login_button(self):
        return WebElementWrapper(self.driver, self.Locators.LOGIN_BUTTON)

    @cached_property
    def error_title(self):
        return WebElementWrapper(self.driver, self.Locators.ERROR_TITLE)

    def login(self, user_type: str = "default"):
        creds = CREDENTIALS[user_type]
        self.username_input.type(creds["username"])
        self.password_input.type(creds["password"])
        self.login_button.click()

    def get_error_message(self):
        return self.error_title.get_text()

    def is_login_successful(self) -> bool:
        try:
            self.wait.for_title_contains("Accounts Overview", timeout=5)
            return True
        except TimeoutException:
            return False

    def get_accounts_overview_title(self) -> str:
        try:
            return self.error_title.get_text()
        except TimeoutException:
            return ""
