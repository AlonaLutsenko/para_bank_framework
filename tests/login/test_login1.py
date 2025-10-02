from framework.constants.credentials import USERNAME, PASSWORD
from framework.constants.urls import BASE_URL
from framework.ui.login_page import LoginPage


def test_login_invalid_user(driver):
    page = LoginPage(driver)
    page.open(BASE_URL)
    page.login(USERNAME, PASSWORD)

    error_text = page.get_error_message()
    assert error_text == "Error!"