from framework.utils.locators import locators


class LoginPageLocators:
    USERNAME_INPUT = locators.name("username")
    PASSWORD_INPUT = locators.name("password")
    LOGIN_BUTTON = locators.css("div.login input.button[value='Log In']")
    ERROR_TITLE = locators.class_name("title")
