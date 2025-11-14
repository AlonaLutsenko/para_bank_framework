from typing import Union

from selenium.common.exceptions import NoSuchElementException

from framework.utils.locators import Locator
from framework.utils.wait import Wait
from framework.utils.web_driver_wrapper import WebDriverWrapper


class WebElementWrapper:
    def __init__(self, driver: WebDriverWrapper, locator: Union[tuple, Locator], wait_timeout: int = 10):
        self.driver = driver
        self.locator = self._normalize_locator(locator)
        self.wait = Wait(driver.driver, timeout=wait_timeout)

    @staticmethod
    def _normalize_locator(locator: Union[tuple, Locator]) -> tuple:
        if isinstance(locator, Locator):
            return locator.as_tuple
        return locator

    def _get_element(self):
        try:
            if isinstance(self.locator, tuple):
                locator_obj = Locator(self.locator[0], self.locator[1])
            else:
                locator_obj = self.locator
            return self.driver.find_element(locator_obj)
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
        except Exception:
            return False

    def wait_for_visible(self, timeout: int = None):
        return self.wait.for_element_visible(self.locator, timeout=timeout)

    def wait_for_clickable(self, timeout: int = None):
        return self.wait.for_element_clickable(self.locator, timeout=timeout)

    def wait_for_invisible(self, timeout: int = None) -> bool:
        return self.wait.for_element_invisible(self.locator, timeout=timeout)
