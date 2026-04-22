from functools import cached_property
from typing import Optional

from selenium.common.exceptions import TimeoutException

from framework.base_page import BasePage
from framework.utils.credentials import get_credentials
from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper
from framework.utils.web_element_wrapper import WebElementWrapper
from ui.components.button import Button
from ui.components.input import Input
from ui.components.text import Text


class LoginPage(BasePage):
    class Locators:
        # Main panels
        MAIN_PANEL = Locator.id("mainPanel")
        TOP_PANEL = Locator.id("topPanel")
        HEADER_PANEL = Locator.id("headerPanel")
        BODY_PANEL = Locator.id("bodyPanel")
        RIGHT_PANEL = Locator.id("rightPanel")
        LOGIN_PANEL = Locator.id("loginPanel")

        # Top panel
        LOGO = Locator.css("img.logo")

        # Navigation buttons
        HOME_BUTTON = Locator.css("ul.button li.home a")
        ABOUT_BUTTON = Locator.css("ul.button li.aboutus a")
        CONTACT_BUTTON = Locator.css("ul.button li.contact a")

        # Left menu
        SOLUTIONS_MENU = Locator.css("ul.leftmenu li.Solutions")
        ABOUT_US_LINK = Locator.css("ul.leftmenu a[href*='about.htm']")
        SERVICES_LINK = Locator.css("ul.leftmenu a[href*='services.htm']")
        PRODUCTS_LINK = Locator.css("ul.leftmenu a[href*='products.jsp']")
        LOCATIONS_LINK = Locator.css("ul.leftmenu a[href*='contacts.jsp']")
        ADMIN_PAGE_LINK = Locator.css("ul.leftmenu a[href*='admin.htm']")

        # Login form
        USERNAME_INPUT = Locator.name("username")
        PASSWORD_INPUT = Locator.name("password")
        LOGIN_BUTTON = Locator.css("div.login input.button[value='Log In']")
        FORGOT_LOGIN_LINK = Locator.css("a[href*='lookup.htm']")
        REGISTER_LINK = Locator.css("a[href*='register.htm']")

        # Right panel - services
        ATM_SERVICES_CAPTION = Locator.css("ul.services li.captionone")
        ONLINE_SERVICES_CAPTION = Locator.css("ul.servicestwo li.captiontwo")

        # Right panel - news
        LATEST_NEWS_HEADING = Locator.css("h4")
        NEWS_DATE = Locator.css("ul.events li.captionthree")
        NEWS_ITEM_REOPENED = Locator.css("ul.events a[href*='news.htm#6']")
        NEWS_ITEM_BILL_PAY = Locator.css("ul.events a[href*='news.htm#5']")
        NEWS_ITEM_TRANSFERS = Locator.css("ul.events a[href*='news.htm#4']")

        ERROR_TITLE = Locator.class_name("title")
        ERROR_BODY = Locator.class_name("error")

    def __init__(self, driver: WebDriverWrapper):
        super().__init__(driver)

    @cached_property
    def username_input(self):
        return Input(self.driver, self.Locators.USERNAME_INPUT)

    @cached_property
    def password_input(self):
        return Input(self.driver, self.Locators.PASSWORD_INPUT)

    @cached_property
    def login_button(self):
        return Button(self.driver, self.Locators.LOGIN_BUTTON)

    @cached_property
    def error_title(self):
        return Text(self.driver, self.Locators.ERROR_TITLE)

    @cached_property
    def error_body(self):
        return Text(self.driver, self.Locators.ERROR_BODY)

    @cached_property
    def main_panel(self):
        return WebElementWrapper(self.driver, self.Locators.MAIN_PANEL)

    @cached_property
    def top_panel(self):
        return WebElementWrapper(self.driver, self.Locators.TOP_PANEL)

    @cached_property
    def header_panel(self):
        return WebElementWrapper(self.driver, self.Locators.HEADER_PANEL)

    @cached_property
    def body_panel(self):
        return WebElementWrapper(self.driver, self.Locators.BODY_PANEL)

    @cached_property
    def right_panel(self):
        return WebElementWrapper(self.driver, self.Locators.RIGHT_PANEL)

    @cached_property
    def login_panel(self):
        return WebElementWrapper(self.driver, self.Locators.LOGIN_PANEL)

    @cached_property
    def logo(self):
        return WebElementWrapper(self.driver, self.Locators.LOGO)

    @cached_property
    def home_button(self):
        return Button(self.driver, self.Locators.HOME_BUTTON)

    @cached_property
    def about_button(self):
        return Button(self.driver, self.Locators.ABOUT_BUTTON)

    @cached_property
    def contact_button(self):
        return Button(self.driver, self.Locators.CONTACT_BUTTON)

    @cached_property
    def solutions_menu(self):
        return WebElementWrapper(self.driver, self.Locators.SOLUTIONS_MENU)

    @cached_property
    def about_us_link(self):
        return WebElementWrapper(self.driver, self.Locators.ABOUT_US_LINK)

    @cached_property
    def services_link(self):
        return WebElementWrapper(self.driver, self.Locators.SERVICES_LINK)

    @cached_property
    def products_link(self):
        return WebElementWrapper(self.driver, self.Locators.PRODUCTS_LINK)

    @cached_property
    def locations_link(self):
        return WebElementWrapper(self.driver, self.Locators.LOCATIONS_LINK)

    @cached_property
    def admin_page_link(self):
        return WebElementWrapper(self.driver, self.Locators.ADMIN_PAGE_LINK)

    @cached_property
    def forgot_login_link(self):
        return WebElementWrapper(self.driver, self.Locators.FORGOT_LOGIN_LINK)

    @cached_property
    def register_link(self):
        return WebElementWrapper(self.driver, self.Locators.REGISTER_LINK)

    @cached_property
    def atm_services_caption(self):
        return Text(self.driver, self.Locators.ATM_SERVICES_CAPTION)

    @cached_property
    def online_services_caption(self):
        return Text(self.driver, self.Locators.ONLINE_SERVICES_CAPTION)

    @cached_property
    def latest_news_heading(self):
        return Text(self.driver, self.Locators.LATEST_NEWS_HEADING)

    @cached_property
    def news_date(self):
        return Text(self.driver, self.Locators.NEWS_DATE)

    @cached_property
    def news_item_reopened(self):
        return Text(self.driver, self.Locators.NEWS_ITEM_REOPENED)

    @cached_property
    def news_item_bill_pay(self):
        return Text(self.driver, self.Locators.NEWS_ITEM_BILL_PAY)

    @cached_property
    def news_item_transfers(self):
        return Text(self.driver, self.Locators.NEWS_ITEM_TRANSFERS)

    def login(self, user_type: str = "default"):
        creds = get_credentials(user_type)
        self.username_input.type(creds["username"])
        self.password_input.type(creds["password"])
        self.login_button.click()

    def enter_username(self, username: str) -> None:
        self.username_input.type(username)

    def enter_password(self, password: str) -> None:
        self.password_input.type(password)

    def submit_login(self) -> None:
        self.login_button.click()

    def clear_username(self) -> None:
        self.username_input.clear()

    def clear_password(self) -> None:
        self.password_input.clear()

    def is_invalid_credentials_error_displayed(self) -> bool:
        title = (self.error_title.get_text() or "").strip()
        body = (self.error_body.get_text() or "").strip()
        return title == "Error!" and body == "The username and password could not be verified."

    def is_empty_fields_validation_error_displayed(self) -> bool:
        title = (self.error_title.get_text() or "").strip()
        body = (self.error_body.get_text() or "").strip()
        return title == "Error!" and body == "Please enter a username and password."

    def is_login_successful(self) -> bool:
        try:
            self.wait.for_title_to_be("ParaBank | Accounts Overview", timeout=10)
            return True
        except TimeoutException:
            return False

    def is_page_loaded(self) -> bool:
        return self.main_panel.is_displayed() and self.login_panel.is_displayed()

    def is_logo_displayed(self) -> bool:
        return self.logo.is_displayed()

    def is_login_form_visible(self) -> bool:
        return (
            self.username_input.verify_element_is_displayed()
            and self.password_input.verify_element_is_displayed()
            and self.login_button.verify_element_is_displayed()
        )

    def is_navigation_visible(self) -> bool:
        return (
            self.home_button.verify_element_is_displayed()
            and self.about_button.verify_element_is_displayed()
            and self.contact_button.verify_element_is_displayed()
        )

    def is_home_button_ready(self) -> bool:
        return self.home_button.verify_element_is_displayed() and self.home_button.verify_element_is_displayed()

    def is_about_button_ready(self) -> bool:
        return self.about_button.verify_element_is_displayed() and self.about_button.verify_element_is_displayed()

    def is_contact_button_ready(self) -> bool:
        return self.contact_button.verify_element_is_displayed() and self.contact_button.verify_element_is_displayed()

    def is_right_panel_visible(self) -> bool:
        return (
            self.right_panel.is_displayed()
            and self.atm_services_caption.verify_element_is_displayed()
            and self.latest_news_heading.verify_element_is_displayed()
        )

    def is_right_panel_displayed(self) -> bool:
        return self.right_panel.is_displayed()

    def is_atm_services_caption_displayed(self) -> bool:
        return self.atm_services_caption.verify_element_is_displayed()

    def is_online_services_caption_displayed(self) -> bool:
        return self.online_services_caption.verify_element_is_displayed()

    def is_latest_news_heading_displayed(self) -> bool:
        return self.latest_news_heading.verify_element_is_displayed()

    def is_left_menu_visible(self) -> bool:
        return (
            self.solutions_menu.is_displayed()
            and self.about_us_link.is_displayed()
            and self.services_link.is_displayed()
        )

    def is_solutions_menu_displayed(self) -> bool:
        return self.solutions_menu.is_displayed()

    def is_about_us_link_displayed(self) -> bool:
        return self.about_us_link.is_displayed()

    def is_services_link_displayed(self) -> bool:
        return self.services_link.is_displayed()

    def is_products_link_displayed(self) -> bool:
        return self.products_link.is_displayed()

    def is_locations_link_displayed(self) -> bool:
        return self.locations_link.is_displayed()

    def is_admin_page_link_displayed(self) -> bool:
        return self.admin_page_link.is_displayed()

    def is_forgot_login_link_displayed(self) -> bool:
        return self.forgot_login_link.is_displayed()

    def is_register_link_displayed(self) -> bool:
        return self.register_link.is_displayed()

    def are_news_items_visible(self) -> bool:
        return (
            self.news_item_reopened.verify_element_is_displayed()
            and self.news_item_bill_pay.verify_element_is_displayed()
            and self.news_item_transfers.verify_element_is_displayed()
        )

    def get_news_date(self) -> Optional[str]:
        return self.news_date.get_text()

    def get_all_panels_visible(self) -> dict:
        return {
            "main_panel": self.main_panel.is_displayed(),
            "top_panel": self.top_panel.is_displayed(),
            "header_panel": self.header_panel.is_displayed(),
            "body_panel": self.body_panel.is_displayed(),
            "right_panel": self.right_panel.is_displayed(),
        }

    def verify_page_structure(self) -> bool:
        panels = self.get_all_panels_visible()
        return all(panels.values())
