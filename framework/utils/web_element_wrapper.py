from typing import Optional

from selenium.webdriver.remote.webelement import WebElement

from framework.utils.locators import Locator
from framework.utils.wait import Wait
from framework.utils.web_driver_wrapper import WebDriverWrapper


class WebElementWrapper:
    def __init__(self, driver: WebDriverWrapper, locator: Locator):
        self.driver = driver
        self.locator = locator
        self.wait = Wait(driver)

    def get_element(self):
        return self.driver.find_element(*self.locator.as_tuple)

    def get_elements(self):
        return self.driver.find_elements(*self.locator.as_tuple)

    def click(self, timeout=None):
        self.wait_for_visible(timeout=timeout).click()

    def clear(self, timeout=None):
        self.wait_for_visible(timeout=timeout).clear()

    def type(self, text: str, timeout=None):
        self.wait_for_visible(timeout=timeout).send_keys(text)

    def get_text(self, timeout=None) -> str:
        return self.wait_for_visible(timeout=timeout).text

    def get_attribute(self, name: str, timeout: Optional[int] = None) -> str | None:
        return self.wait_for_visible(timeout).get_attribute(name)

    def is_displayed(self) -> bool:
        return self.get_element().is_displayed()

    def wait_for_visible(self, timeout: Optional[int] = None) -> WebElement:
        return self.wait.for_element_visible(self.locator, timeout=timeout)

    def wait_for_clickable(self, timeout: Optional[int] = None) -> WebElement:
        return self.wait.for_element_clickable(self.locator, timeout=timeout)

    def wait_for_invisible(self, timeout: Optional[int] = None) -> bool:
        return self.wait.for_element_invisible(self.locator, timeout=timeout)
