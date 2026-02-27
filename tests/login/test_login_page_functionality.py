from framework.utils.allure_helper import case, step
from framework.utils.urls import get_base_url
from ui.pages.login_page import LoginPage


@case("Login Page", "Form Interaction", "Input Field Operations")
def test_login_form_interaction(driver):
    with step("Open login page"):
        page = LoginPage(driver)
        page.open(get_base_url())

    with step("Verify login form is ready"):
        assert page.can_login(), "Should be able to login"

    with step("Test input field operations"):
        page.enter_username("test_user")
        assert page.get_username_value() == "test_user", "Username value should be set correctly"

        page.clear_username()
        assert page.get_username_value() == "", "Username should be cleared"

        page.clear_and_type_username("new_user")
        assert page.get_username_value() == "new_user", "Username should be updated after clear_and_type"


@case("Login Page", "Content Retrieval", "Text Elements")
def test_text_elements_retrieval(driver):
    with step("Open login page"):
        page = LoginPage(driver)
        page.open(get_base_url())

    with step("Retrieve and verify text elements"):
        caption = page.get_caption_text()
        assert caption is not None, "Caption text should not be None"

        atm_caption = page.get_atm_services_caption()
        assert atm_caption is not None, "ATM services caption should not be None"

        online_caption = page.get_online_services_caption()
        assert online_caption is not None, "Online services caption should not be None"

        news_heading = page.get_latest_news_heading()
        assert news_heading is not None, "Latest news heading should not be None"

        news_items = ["reopened", "bill_pay", "transfers"]
        for item in news_items:
            text = page.get_news_item_text(item)
            assert text is not None, f"News item '{item}' text should not be None"
