from selenium.common.exceptions import NoSuchElementException, TimeoutException

from framework.utils.locators import Locator
from framework.utils.wait import Wait
from framework.utils.web_driver_wrapper import WebDriverWrapper


class WebElementWrapper:
    def __init__(self, driver: WebDriverWrapper, locator: Locator):
        self.driver = driver
        self.locator = locator
        self.wait = Wait(driver)

    def _get_element(self):
        try:
            return self.driver.find_element(self.locator)
        except NoSuchElementException:
            raise RuntimeError(f"Element not found: {self.locator}")

    def _wait_and_get_element(self):
        return self.wait.for_element_visible(self.locator)

    def click(self):
        self.wait.for_element_clickable(self.locator).click()

    def type(self, text: str):
        element = self.wait.for_element_visible(self.locator)
        element.clear()
        element.send_keys(text)

    def get_text(self) -> str:
        return self.wait.for_element_visible(self.locator).text

    def is_displayed(self) -> bool:
        try:
            element = self.wait.for_element_present(self.locator, timeout=2)
            return element.is_displayed()
        except TimeoutException:
            return False

    def wait_for_visible(self, timeout: int = None):
        return self.wait.for_element_visible(self.locator, timeout=timeout)

    def wait_for_clickable(self, timeout: int = None):
        return self.wait.for_element_clickable(self.locator, timeout=timeout)

    def wait_for_invisible(self, timeout: int = None) -> bool:
        return self.wait.for_element_invisible(self.locator, timeout=timeout)
