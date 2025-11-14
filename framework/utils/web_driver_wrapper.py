from selenium.common.exceptions import TimeoutException

from framework.utils.locators import Locator


class WebDriverWrapper:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        try:
            self.driver.get(url)
        except TimeoutException:
            raise RuntimeError(f"Page load timeout: {url}")

    def find_element(self, locator: Locator):
        return self.driver.find_element(*locator.as_tuple)
