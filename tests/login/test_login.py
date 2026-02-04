import allure

from framework.constants.urls import BASE_URL
from ui.pages.login_page import LoginPage


@allure.epic("Login")
@allure.feature("User Authentication")
@allure.story("Valid Login")
def test_login_valid_user(driver):
    with allure.step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with allure.step("Verify login form is visible"):
        assert page.is_login_form_visible(), "Login form should be visible"

    with allure.step("Perform login with valid credentials"):
        page.login(user_type="default")

    with allure.step("Verify login was successful"):
        assert page.is_login_successful(), "Login was not successful"


@allure.epic("Login")
@allure.feature("User Authentication")
@allure.story("Invalid Credentials")
def test_login_invalid_credentials(driver):
    with allure.step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with allure.step("Enter invalid credentials"):
        page.enter_username("invalid_user")
        page.enter_password("invalid_password")
        page.submit_login()

    with allure.step("Verify error message is displayed"):
        error_message = page.get_error_message()
        assert error_message is not None, "Error message should be displayed for invalid credentials"
        assert len(error_message) > 0, "Error message should not be empty"


@allure.epic("Login")
@allure.feature("User Authentication")
@allure.story("Empty Fields Validation")
def test_login_with_empty_fields(driver):
    with allure.step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with allure.step("Clear all fields and submit"):
        page.clear_username()
        page.clear_password()
        page.submit_login()

    with allure.step("Verify error message is displayed"):
        error_message = page.get_error_message()
        assert error_message is not None, "Error message should be displayed for empty login"
