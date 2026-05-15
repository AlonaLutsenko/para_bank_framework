from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper
from framework.utils.web_element_wrapper import WebElementWrapper


class BaseComponent:
    def __init__(self, driver: WebDriverWrapper, locator: Locator):
        self.driver = driver
        self.locator = locator

    @property
    def element(self) -> WebElementWrapper:
        return WebElementWrapper(self.driver, self.locator)

    def click(self, timeout=None):
        self.element.click(timeout=timeout)

    def verify_element_is_displayed(self, displayed=True, timeout=None):
        if displayed:
            return self.element.wait_for_visible(timeout=timeout)
        return self.element.wait_for_invisible(timeout=timeout)
