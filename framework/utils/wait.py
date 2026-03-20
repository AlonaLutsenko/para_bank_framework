from typing import Any, Callable, Optional

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.types import WaitExcTypes
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper


class Wait:

    def __init__(
        self,
        driver: WebDriverWrapper,
        timeout: int = 10,
        poll_frequency: float = 0.5,
        ignored_exceptions: Optional[WaitExcTypes] = None,
    ):
        self.driver = driver
        self.timeout = timeout
        self.poll_frequency = poll_frequency
        if ignored_exceptions is None:
            self.ignored_exceptions = [
                StaleElementReferenceException,
                NoSuchElementException,
            ]
        else:
            self.ignored_exceptions = ignored_exceptions
        self._wait = self._create_wait(timeout)

    def _create_wait(self, timeout: Optional[int] = None) -> WebDriverWait:
        timeout = timeout if timeout is not None else self.timeout
        kwargs = {
            "driver": self.driver.driver,
            "timeout": timeout,
            "poll_frequency": self.poll_frequency,
            "ignored_exceptions": self.ignored_exceptions,
        }
        return WebDriverWait(**kwargs)

    def _get_wait(self, timeout: Optional[int] = None) -> WebDriverWait:
        return self._wait if timeout is None else self._create_wait(timeout)

    def until(self, method: Callable, message: str = "") -> Any:
        return self._wait.until(method, message=message)

    def for_element_visible(self, locator: Locator, timeout: Optional[int] = None) -> WebElement:
        wait = self._get_wait(timeout)
        return wait.until(EC.visibility_of_element_located(locator.as_tuple))

    def for_element_present(self, locator: Locator, timeout: Optional[int] = None) -> WebElement:
        wait = self._get_wait(timeout)
        return wait.until(EC.presence_of_element_located(locator.as_tuple))

    def for_element_clickable(self, locator: Locator, timeout: Optional[int] = None) -> WebElement:
        wait = self._get_wait(timeout)
        return wait.until(EC.element_to_be_clickable(locator.as_tuple))

    def for_element_invisible(self, locator: Locator, timeout: Optional[int] = None) -> WebElement | bool:
        wait = self._get_wait(timeout)
        return wait.until(EC.invisibility_of_element_located(locator.as_tuple))

    def for_element_to_disappear(self, locator: Locator, timeout: Optional[int] = None) -> bool:
        wait = self._get_wait(timeout)
        element = self.driver.driver.find_element(*locator.as_tuple)
        return wait.until(EC.staleness_of(element))

    def for_text_in_element(self, locator: Locator, text: str, timeout: Optional[int] = None) -> bool:
        wait = self._get_wait(timeout)
        return wait.until(EC.text_to_be_present_in_element(locator.as_tuple, text))

    def for_title_contains(self, title_fragment: str, timeout: Optional[int] = None) -> bool:
        wait = self._get_wait(timeout)
        return wait.until(EC.title_contains(title_fragment))

    def for_title_to_be(self, title: str, timeout: Optional[int] = None) -> bool:
        wait = self._get_wait(timeout)
        return wait.until(EC.title_is(title))

    def for_alert_present(self, timeout: Optional[int] = None):
        wait = self._get_wait(timeout)
        return wait.until(EC.alert_is_present())

    def for_element_to_have_attribute(
        self, locator: Locator, attribute: str, value: str, timeout: Optional[int] = None
    ) -> bool:
        wait = self._get_wait(timeout)

        def _check_attribute(driver):
            try:
                element = driver.find_element(*locator.as_tuple)
                return element.get_attribute(attribute) == value
            except (StaleElementReferenceException, NoSuchElementException):
                return False

        return wait.until(_check_attribute)

    def for_element_to_be_selected(self, locator: Locator, timeout: Optional[int] = None) -> bool:
        wait = self._get_wait(timeout)
        return wait.until(EC.element_located_to_be_selected(locator.as_tuple))

    def with_custom_condition(self, condition: Callable, timeout: Optional[int] = None) -> Any:
        wait = self._get_wait(timeout)
        return wait.until(condition)
