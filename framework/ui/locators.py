from selenium.webdriver.common.by import By


class Locator:
    def __init__(self, by: By, value: str):
        self.by = by
        self.value = value

    def as_tuple(self):
        return self.by, self.value


class LoginPageLocators:
    USERNAME_INPUT = Locator(By.NAME, "username")
    PASSWORD_INPUT = Locator(By.NAME, "password")
    LOGIN_BUTTON = Locator(
        By.CSS_SELECTOR, "div.login input.button[value='Log In']"
    )  # noqa: E501
    ERROR_TITLE = Locator(By.CLASS_NAME, "title")
