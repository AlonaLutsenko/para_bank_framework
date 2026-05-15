from framework.utils.allure_helper import case, step
from ui.pages.login_page import LoginPage


@case("Login Page", "Page Structure", "Page Elements Visibility")
def test_page_structure_and_elements(login_page: LoginPage):
    with step("Verify page structure"):
        assert login_page.is_page_loaded(), "Login page did not load properly"
        assert login_page.verify_page_structure(), "Page structure is not complete"
        assert login_page.is_logo_displayed(), "Logo is not displayed"
        assert login_page.is_login_form_visible(), "Login form is not visible"
        assert login_page.is_navigation_visible(), "Navigation buttons are not visible"
        assert login_page.is_right_panel_visible(), "Right panel is not visible"
        assert login_page.is_left_menu_visible(), "Left menu is not visible"


@case("Login Page", "Navigation", "Navigation Buttons")
def test_navigation_elements(login_page: LoginPage):
    with step("Verify navigation buttons"):
        assert login_page.is_home_button_ready(), "Home button should be displayed and enabled"
        assert login_page.is_about_button_ready(), "About button should be displayed and enabled"
        assert login_page.is_contact_button_ready(), "Contact button should be displayed and enabled"


@case("Login Page", "Left Menu", "Menu Elements Visibility")
def test_left_menu_elements(login_page: LoginPage):
    with step("Verify left menu elements"):
        assert login_page.is_solutions_menu_displayed(), "Solutions menu is not displayed"
        assert login_page.is_about_us_link_displayed(), "About Us link is not displayed"
        assert login_page.is_services_link_displayed(), "Services link is not displayed"
        assert login_page.is_products_link_displayed(), "Products link is not displayed"
        assert login_page.is_locations_link_displayed(), "Locations link is not displayed"
        assert login_page.is_admin_page_link_displayed(), "Admin page link is not displayed"


@case("Login Page", "Right Panel", "Services Section")
def test_right_panel_services(login_page: LoginPage):
    with step("Verify right panel services"):
        assert login_page.is_right_panel_displayed(), "Right panel is not displayed"
        assert (
            login_page.is_atm_services_caption_displayed() and login_page.is_online_services_caption_displayed()
        ), "At least one services caption should be displayed"


@case("Login Page", "Right Panel", "News Section")
def test_news_section(login_page: LoginPage):
    with step("Verify news section"):
        assert login_page.is_latest_news_heading_displayed(), "Latest News heading is not displayed"
        assert login_page.are_news_items_visible(), "News items are not visible"
        news_date = login_page.get_news_date()
        assert news_date is not None, "News date is None"
