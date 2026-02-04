from typing import Optional

from selenium.common.exceptions import TimeoutException

from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper
from ui.components.base_component import BaseComponent


class Text(BaseComponent):
    def __init__(self, driver: WebDriverWrapper, locator: Locator):
        super().__init__(driver, locator)

    def get_text(self) -> Optional[str]:
        try:
            return self.element.get_text()
        except TimeoutException:
            return None
