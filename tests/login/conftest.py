import pytest

from framework.utils.allure_helper import step
from framework.utils.urls import get_base_url
from ui.pages.login_page import LoginPage


@pytest.fixture
def login_page(driver):
    with step("Open login page"):
        page = LoginPage(driver)
        page.open(get_base_url())
        return page
