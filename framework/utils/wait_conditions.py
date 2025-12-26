from typing import Callable, Tuple

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class WaitConditions:

    @staticmethod
    def element_is_stale(element: WebElement) -> Callable:
        def _condition(driver: WebDriver) -> bool:
            try:
                element.is_enabled()
                return False
            except StaleElementReferenceException:
                return True

        return _condition

    @staticmethod
    def element_text_not_empty(locator: Tuple[str, str]) -> Callable:
        def _condition(driver: WebDriver) -> bool:
            element = driver.find_element(*locator)
            return bool(element.text.strip())

        return _condition

    @staticmethod
    def element_value_equals(locator: Tuple[str, str], expected_value: str) -> Callable:
        def _condition(driver: WebDriver) -> bool:
            element = driver.find_element(*locator)
            return element.get_attribute("value") == expected_value

        return _condition

    @staticmethod
    def page_load_complete() -> Callable:
        def _condition(driver: WebDriver) -> bool:
            return driver.execute_script("return document.readyState") == "complete"

        return _condition

    @staticmethod
    def element_is_enabled(locator: Tuple[str, str]) -> Callable:
        def _condition(driver: WebDriver) -> bool:
            element = driver.find_element(*locator)
            return element.is_enabled()

        return _condition

    @staticmethod
    def element_is_disabled(locator: Tuple[str, str]) -> Callable:
        def _condition(driver: WebDriver) -> bool:
            element = driver.find_element(*locator)
            return not element.is_enabled()

        return _condition
