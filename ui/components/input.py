from typing import Optional

from framework.utils.decorators import return_on_timeout
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

    @return_on_timeout(None)
    def get_value(self) -> Optional[str]:
        return self.element.get_attribute("value", timeout=2)

    @return_on_timeout(None)
    def get_placeholder(self) -> Optional[str]:
        return self.element.get_attribute("placeholder", timeout=2)

    @return_on_timeout(False)
    def is_enabled(self) -> bool:
        element = self.element.wait_for_clickable(timeout=2)
        return element.is_enabled()

    @return_on_timeout(False)
    def is_readonly(self) -> bool:
        return self.element.get_attribute("readonly", timeout=2) is not None
