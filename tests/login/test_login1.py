from framework.constants.urls import BASE_URL
from framework.ui.login_page import LoginPage


def test_login_invalid_user(driver):
    page = LoginPage(driver)
    page.open(BASE_URL)

    page.login(user_type="default")

    error_text = page.get_error_message()
    assert error_text == "Error!", f"Unexpected error message: {error_text}"
