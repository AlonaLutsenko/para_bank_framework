from framework.constants.urls import BASE_URL
from ui.pages.login_page import LoginPage


def test_login_valid_user(driver):
    page = LoginPage(driver)
    page.open(BASE_URL)

    page.login(user_type="default")

    assert page.is_login_successful(), "Login was not successful"
    title_text = page.get_accounts_overview_title()
    assert title_text == "Accounts Overview", f"Expected 'Accounts Overview', but got: {title_text}"
