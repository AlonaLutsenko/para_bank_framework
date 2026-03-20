from typing import Optional

from framework.utils.decorators import return_on_timeout
from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper
from ui.components.base_component import BaseComponent


class Button(BaseComponent):
    def __init__(self, driver: WebDriverWrapper, locator: Locator):
        super().__init__(driver, locator)

    def click(self):
        self.element.click()

    @return_on_timeout(False)
    def is_enabled(self) -> bool:
        element = self.element.wait_for_clickable(timeout=2)
        return element.is_enabled()

    @return_on_timeout(False)
    def is_clickable(self) -> bool:
        self.element.wait_for_clickable(timeout=2)
        return True

    def is_disabled(self) -> bool:
        return not self.is_enabled()

    @return_on_timeout(None)
    def get_value(self) -> Optional[str]:
        return self.element.get_attribute("value", timeout=2)
