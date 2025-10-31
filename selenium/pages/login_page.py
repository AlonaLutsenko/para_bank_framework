from functools import cached_property

from framework.constants.credentials import CREDENTIALS
from framework.utils.base_page import BasePage
from framework.utils.web_element_wrapper import WebElementWrapper
from selenium.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @cached_property
    def username_input(self):
        return WebElementWrapper(self.driver, LoginPageLocators.USERNAME_INPUT.as_tuple())

    @cached_property
    def password_input(self):
        return WebElementWrapper(self.driver, LoginPageLocators.PASSWORD_INPUT.as_tuple())

    @cached_property
    def login_button(self):
        return WebElementWrapper(self.driver, LoginPageLocators.LOGIN_BUTTON.as_tuple())

    @cached_property
    def error_title(self):
        return WebElementWrapper(self.driver, LoginPageLocators.ERROR_TITLE.as_tuple())

    def login(self, user_type: str = "default"):
        creds = CREDENTIALS[user_type]
        self.username_input.type(creds["username"])
        self.password_input.type(creds["password"])
        self.login_button.click()

    def get_error_message(self):
        return self.error_title.get_text()
