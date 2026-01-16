import allure

from framework.constants.urls import BASE_URL
from ui.pages.login_page import LoginPage


@allure.epic("Login Page")
@allure.feature("Page Structure")
@allure.story("Page Elements Visibility")
def test_page_structure_and_elements(driver):
    with allure.step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with allure.step("Verify page structure"):
        assert page.is_page_loaded(), "Login page did not load properly"
        assert page.verify_page_structure(), "Page structure is not complete"
        assert page.is_logo_displayed(), "Logo is not displayed"
        assert page.is_login_form_visible(), "Login form is not visible"
        assert page.is_navigation_visible(), "Navigation buttons are not visible"
        assert page.is_right_panel_visible(), "Right panel is not visible"
        assert page.is_left_menu_visible(), "Left menu is not visible"


@allure.epic("Login Page")
@allure.feature("Login Form")
@allure.story("Form Elements Visibility")
def test_login_form_elements(driver):
    with allure.step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with allure.step("Verify login form elements"):
        assert page.username_input.is_displayed(), "Username input is not displayed"
        assert page.password_input.is_displayed(), "Password input is not displayed"
        assert page.login_button.is_displayed(), "Login button is not displayed"
        assert page.login_button.is_enabled(), "Login button should be enabled"
        assert page.username_input.is_enabled(), "Username input should be enabled"
        assert page.password_input.is_enabled(), "Password input should be enabled"
        assert page.forgot_login_link.is_displayed(), "Forgot login link is not displayed"
        assert page.register_link.is_displayed(), "Register link is not displayed"


@allure.epic("Login Page")
@allure.feature("Navigation")
@allure.story("Navigation Buttons")
def test_navigation_elements(driver):
    with allure.step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with allure.step("Verify navigation buttons"):
        assert (
            page.home_button.is_displayed() and page.home_button.is_enabled()
        ), "Home button should be displayed and enabled"
        assert (
            page.about_button.is_displayed() and page.about_button.is_enabled()
        ), "About button should be displayed and enabled"
        assert (
            page.contact_button.is_displayed() and page.contact_button.is_enabled()
        ), "Contact button should be displayed and enabled"


@allure.epic("Login Page")
@allure.feature("Left Menu")
@allure.story("Menu Elements Visibility")
def test_left_menu_elements(driver):
    with allure.step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with allure.step("Verify left menu elements"):
        assert page.solutions_menu.is_displayed(), "Solutions menu is not displayed"
        assert page.about_us_link.is_displayed(), "About Us link is not displayed"
        assert page.services_link.is_displayed(), "Services link is not displayed"
        assert page.products_link.is_displayed(), "Products link is not displayed"
        assert page.locations_link.is_displayed(), "Locations link is not displayed"
        assert page.admin_page_link.is_displayed(), "Admin page link is not displayed"


@allure.epic("Login Page")
@allure.feature("Right Panel")
@allure.story("Services Section")
def test_right_panel_services(driver):
    with allure.step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with allure.step("Verify right panel services"):
        assert page.right_panel.is_displayed(), "Right panel is not displayed"
        assert (
            page.atm_services_caption.is_displayed() or page.online_services_caption.is_displayed()
        ), "At least one services caption should be displayed"


@allure.epic("Login Page")
@allure.feature("Right Panel")
@allure.story("News Section")
def test_news_section(driver):
    with allure.step("Open login page"):
        page = LoginPage(driver)
        page.open(BASE_URL)

    with allure.step("Verify news section"):
        assert page.latest_news_heading.is_displayed(), "Latest News heading is not displayed"
        assert page.are_news_items_visible(), "News items are not visible"
        news_date = page.get_news_date()
        assert news_date is not None, "News date is None"
