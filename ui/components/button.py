from typing import Optional

from selenium.common.exceptions import TimeoutException

from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper
from ui.components.base_component import BaseComponent


class Button(BaseComponent):
    def __init__(self, driver: WebDriverWrapper, locator: Locator):
        super().__init__(driver, locator)

    def click(self):
        self.element.click()

    def is_enabled(self) -> bool:
        try:
            element = self.element.wait_for_clickable(timeout=2)
            return element.is_enabled()
        except TimeoutException:
            return False

    def is_clickable(self) -> bool:
        try:
            self.element.wait_for_clickable(timeout=2)
            return True
        except TimeoutException:
            return False

    def is_disabled(self) -> bool:
        return not self.is_enabled()

    def get_value(self) -> Optional[str]:
        try:
            element = self.element.wait_for_visible(timeout=2)
            return element.get_attribute("value")
        except TimeoutException:
            return None
