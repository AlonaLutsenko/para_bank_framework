from typing import Any, Callable, Optional, Tuple, Union

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from framework.utils.locators import Locator


class Wait:

    def __init__(self, driver: WebDriver, timeout: int = 10, poll_frequency: float = 0.5):
        self.driver = driver
        self.timeout = timeout
        self.poll_frequency = poll_frequency
        self._wait = WebDriverWait(driver, timeout, poll_frequency=poll_frequency)

    @staticmethod
    def _normalize_locator(locator: Union[Tuple[str, str], Locator]) -> Tuple[str, str]:
        if isinstance(locator, Locator):
            return locator.as_tuple
        return locator

    def until(self, method: Callable, message: str = "") -> Any:
        return self._wait.until(method, message=message)

    def for_element_visible(
        self, locator: Union[Tuple[str, str], Locator], timeout: Optional[int] = None
    ) -> WebElement:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        locator_tuple = self._normalize_locator(locator)
        return wait.until(EC.visibility_of_element_located(locator_tuple))

    def for_element_present(
        self, locator: Union[Tuple[str, str], Locator], timeout: Optional[int] = None
    ) -> WebElement:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        locator_tuple = self._normalize_locator(locator)
        return wait.until(EC.presence_of_element_located(locator_tuple))

    def for_element_clickable(
        self, locator: Union[Tuple[str, str], Locator], timeout: Optional[int] = None
    ) -> WebElement:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        locator_tuple = self._normalize_locator(locator)
        return wait.until(EC.element_to_be_clickable(locator_tuple))

    def for_element_invisible(self, locator: Union[Tuple[str, str], Locator], timeout: Optional[int] = None) -> bool:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        locator_tuple = self._normalize_locator(locator)
        return wait.until(EC.invisibility_of_element_located(locator_tuple))

    def for_element_to_disappear(self, locator: Union[Tuple[str, str], Locator], timeout: Optional[int] = None) -> bool:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        locator_tuple = self._normalize_locator(locator)
        return wait.until(EC.staleness_of(self.driver.find_element(*locator_tuple)))

    def for_text_in_element(
        self, locator: Union[Tuple[str, str], Locator], text: str, timeout: Optional[int] = None
    ) -> bool:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        locator_tuple = self._normalize_locator(locator)
        return wait.until(EC.text_to_be_present_in_element(locator_tuple, text))

    def for_title_contains(self, title_fragment: str, timeout: Optional[int] = None) -> bool:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        return wait.until(EC.title_contains(title_fragment))

    def for_title_to_be(self, title: str, timeout: Optional[int] = None) -> bool:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        return wait.until(EC.title_is(title))

    def for_alert_present(self, timeout: Optional[int] = None):
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        return wait.until(EC.alert_is_present())

    def for_element_to_have_attribute(
        self, locator: Union[Tuple[str, str], Locator], attribute: str, value: str, timeout: Optional[int] = None
    ) -> bool:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        locator_tuple = self._normalize_locator(locator)

        def _check_attribute(driver):
            try:
                element = driver.find_element(*locator_tuple)
                return element.get_attribute(attribute) == value
            except (StaleElementReferenceException, Exception):
                return False

        return wait.until(_check_attribute)

    def for_element_to_be_selected(
        self, locator: Union[Tuple[str, str], Locator], timeout: Optional[int] = None
    ) -> bool:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        locator_tuple = self._normalize_locator(locator)
        return wait.until(EC.element_located_to_be_selected(locator_tuple))

    def with_custom_condition(self, condition: Callable, timeout: Optional[int] = None) -> Any:
        wait = (
            self._wait if timeout is None else WebDriverWait(self.driver, timeout, poll_frequency=self.poll_frequency)
        )
        return wait.until(condition)
