from typing import Optional

from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper
from ui.components.base_component import BaseComponent


class Input(BaseComponent):
    def __init__(self, driver: WebDriverWrapper, locator: Locator):
        super().__init__(driver, locator)

    def type(self, text: str):
        self.element.type(text)

    def clear(self):
        self.element.clear()

    def clear_and_type(self, text: str):
        self.clear()
        self.type(text)

    def get_value(self) -> Optional[str]:
        return self.element.get_attribute("value", timeout=2)

    def get_placeholder(self) -> Optional[str]:
        return self.element.get_attribute("placeholder", timeout=2)

    def is_disabled(self) -> bool:
        return not self.verify_element_is_displayed().is_enabled()

    def is_readonly(self) -> bool:
        return self.element.get_attribute("readonly", timeout=2) is not None
