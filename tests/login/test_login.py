from framework.constants.urls import BASE_URL
from framework.utils.allure_helper import case, step
from ui.pages.login_page import LoginPage


@case("Login", "User Authentication", "Valid Login")
def test_login_valid_user(driver):
    with step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with step("Verify login form is visible"):
        assert page.is_login_form_visible(), "Login form should be visible"

    with step("Perform login with valid credentials"):
        page.login(user_type="default")

    with step("Verify login was successful"):
        assert page.is_login_successful(), "Login was not successful"


@case("Login", "User Authentication", "Invalid Credentials")
def test_login_invalid_credentials(driver):
    with step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with step("Enter invalid credentials"):
        page.enter_username("invalid_user")
        page.enter_password("invalid_password")
        page.submit_login()

    with step("Verify error message is displayed"):
        error_message = page.get_error_message()
        assert error_message is not None, "Error message should be displayed for invalid credentials"
        assert len(error_message) > 0, "Error message should not be empty"


@case("Login", "User Authentication", "Empty Fields Validation")
def test_login_with_empty_fields(driver):
    with step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with step("Clear all fields and submit"):
        page.clear_username()
        page.clear_password()
        page.submit_login()

    with step("Verify error message is displayed"):
        error_message = page.get_error_message()
        assert error_message is not None, "Error message should be displayed for empty login"
