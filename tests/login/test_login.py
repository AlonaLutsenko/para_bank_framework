from framework.utils.allure_helper import case, step
from ui.pages.login_page import LoginPage


@case("Login", "User Authentication", "Valid Login")
def test_login_valid_user(login_page: LoginPage):
    with step("Perform login with valid credentials"):
        login_page.login(user_type="default")

    with step("Verify login was successful"):
        assert login_page.is_login_successful(), "Login was not successful"


@case("Login", "User Authentication", "Invalid Credentials")
def test_login_invalid_credentials(login_page: LoginPage):
    with step("Enter invalid credentials"):
        login_page.enter_username("invalid_user")
        login_page.enter_password("invalid_password")
        login_page.submit_login()

    with step("Verify error message is displayed"):
        assert login_page.is_invalid_credentials_error_displayed(), "Expected invalid-credentials error title and body"


@case("Login", "User Authentication", "Empty Fields Validation")
def test_login_with_empty_fields(login_page: LoginPage):
    with step("Clear all fields and submit"):
        login_page.clear_username()
        login_page.clear_password()
        login_page.submit_login()

    with step("Verify error message is displayed"):
        assert (
            login_page.is_empty_fields_validation_error_displayed()
        ), "Expected empty-fields validation error title and body"
