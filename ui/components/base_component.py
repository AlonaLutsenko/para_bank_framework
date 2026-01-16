from typing import Optional

from selenium.common.exceptions import TimeoutException

from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper
from framework.utils.web_element_wrapper import WebElementWrapper


class BaseComponent:
    def __init__(self, driver: WebDriverWrapper, locator: Locator):
        self.driver = driver
        self.locator = locator
        self._element = WebElementWrapper(driver, locator)

    @property
    def element(self) -> WebElementWrapper:
        return self._element

    def click(self):
        self._element.click()

    def is_displayed(self) -> bool:
        return self._element.is_displayed()

    def wait_for_visible(self, timeout: int = None):
        return self._element.wait_for_visible(timeout=timeout)

    def wait_for_clickable(self, timeout: int = None):
        return self._element.wait_for_clickable(timeout=timeout)

    def wait_for_invisible(self, timeout: int = None) -> bool:
        return self._element.wait_for_invisible(timeout=timeout)

    def get_text(self) -> Optional[str]:
        try:
            return self._element.get_text()
        except TimeoutException:
            return None
