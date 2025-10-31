from selenium.locators import Locator


class LoginPageLocators:
    USERNAME_INPUT = Locator.name("username")
    PASSWORD_INPUT = Locator.name("password")
    LOGIN_BUTTON = Locator.css("div.login input.button[value='Log In']")
    ERROR_TITLE = Locator.class_name("title")
