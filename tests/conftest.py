import pytest

from framework.run_config import RunConfig
from framework.utils.allure_helper import step
from ui.pages.login_page import LoginPage


@pytest.fixture
def login_page(driver):
    with step("Open login page"):
        page = LoginPage(driver)
        page.open(RunConfig.base_url())
        return page
