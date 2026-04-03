import pytest

from framework.utils.appsettings import load_appsettings
from framework.utils.driver_factory import DriverFactory
from framework.utils.web_driver_wrapper import WebDriverWrapper


def pytest_configure(config):
    """Load appsettings once at session start so missing config fails before collection or browser work."""
    load_appsettings()


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    raw_driver = DriverFactory.create_driver(browser, headless=headless)
    driver = WebDriverWrapper(raw_driver)
    yield driver
    if hasattr(driver, 'driver') and driver.driver:
        driver.driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=None,
        help="Run browser in headless mode",
    )
