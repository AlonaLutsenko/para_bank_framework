import pytest
from framework.utils.driver_factory import DriverFactory

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser") or "chrome"
    driver = DriverFactory.create_driver(browser)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")