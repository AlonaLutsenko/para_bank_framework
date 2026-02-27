from framework.utils.allure_helper import case, step
from ui.pages.login_page import LoginPage


@case("Login Page", "Form Interaction", "Input Field Operations")
def test_login_form_interaction(login_page: LoginPage):
    with step("Verify login form is ready"):
        assert login_page.can_login(), "Login form should be ready"

    with step("Test input field operations"):
        login_page.enter_username("test_user")
        assert login_page.get_username_value() == "test_user", "Username value should be set correctly"

        login_page.clear_username()
        assert login_page.get_username_value() == "", "Username should be cleared"

        login_page.clear_and_type_username("new_user")
        assert login_page.get_username_value() == "new_user", "Username should be updated after clear_and_type"


@case("Login Page", "Content Retrieval", "Text Elements")
def test_text_elements_retrieval(login_page: LoginPage):
    with step("Retrieve and verify text elements"):
        caption = login_page.get_caption_text()
        assert caption is not None, "Caption text should not be None"

        atm_caption = login_page.get_atm_services_caption()
        assert atm_caption is not None, "ATM services caption should not be None"

        online_caption = login_page.get_online_services_caption()
        assert online_caption is not None, "Online services caption should not be None"

        news_heading = login_page.get_latest_news_heading()
        assert news_heading is not None, "Latest news heading should not be None"

        news_items = ["reopened", "bill_pay", "transfers"]
        for item in news_items:
            text = login_page.get_news_item_text(item)
            assert text is not None, f"News item '{item}' text should not be None"
