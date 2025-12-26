import pytest

from framework.utils.driver_factory import DriverFactory
from framework.utils.web_driver_wrapper import WebDriverWrapper


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    raw_driver = DriverFactory.create_driver(browser)
    driver = WebDriverWrapper(raw_driver)
    yield driver
    driver.driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests",
    )
