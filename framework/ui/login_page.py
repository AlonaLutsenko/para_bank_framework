from framework.constants.credentials import CREDENTIALS
from framework.ui.base_page import BasePage
from framework.ui.locators import LoginPageLocators
from framework.utils.web_element_wrapper import WebElementWrapper


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = WebElementWrapper(
            driver, LoginPageLocators.USERNAME_INPUT.as_tuple()
        )
        self.password_input = WebElementWrapper(
            driver, LoginPageLocators.PASSWORD_INPUT.as_tuple()
        )
        self.login_button = WebElementWrapper(
            driver, LoginPageLocators.LOGIN_BUTTON.as_tuple()
        )
        self.error_title = WebElementWrapper(
            driver, LoginPageLocators.ERROR_TITLE.as_tuple()
        )

    def open(self, url):
        self.driver.open(url)

    def login(self, user_type: str = "default"):
        creds = CREDENTIALS[user_type]
        self.username_input.type(creds["username"])
        self.password_input.type(creds["password"])
        self.login_button.click()

    def get_error_message(self):
        return self.error_title.get_text()
