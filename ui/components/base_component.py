from typing import Optional

from selenium.webdriver.remote.webelement import WebElement

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
        self._element.wait_for_visible(5)
        return self._element

    def is_present(self) -> bool:
        return self._element.is_present()

    def is_displayed(self) -> bool:
        return self._element.is_displayed()

    def wait_for_visible(self, timeout: Optional[int] = None) -> WebElement:
        return self._element.wait_for_visible(timeout=timeout)

    def wait_for_invisible(self, timeout: Optional[int] = None) -> bool:
        return self._element.wait_for_invisible(timeout=timeout)
