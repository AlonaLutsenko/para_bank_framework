import pytest

from framework.run_config import RunConfig
from framework.utils.driver_factory import DriverFactory
from framework.utils.web_driver_wrapper import WebDriverWrapper


def pytest_configure(config):
    """Load appsettings once at session start so missing config fails before collection or browser work."""
    RunConfig.set_run_config(
        base_url="https://parabank.parasoft.com",
        browser=config.getoption("--browser"),
        headless=config.getoption("--headless"),
        remote=config.getoption("--remote"),
    )


@pytest.fixture
def driver(request):
    browser = RunConfig.browser()
    headless = RunConfig.headless()
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
        default=False,
        help="Run browser in headless mode",
    )
    parser.addoption(
        "--remote",
        action="store_true",
        default=False,
        help="",
    )
