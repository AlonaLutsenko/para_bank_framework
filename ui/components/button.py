from typing import Optional

from selenium.webdriver.remote.webelement import WebElement

from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper
from ui.components.base_component import BaseComponent


class Button(BaseComponent):
    def __init__(self, driver: WebDriverWrapper, locator: Locator):
        super().__init__(driver, locator)

    def is_clickable(self) -> WebElement:
        return self.element.wait_for_clickable(timeout=2)

    def is_disabled(self) -> bool:
        return not self.verify_element_is_displayed().is_enabled()

    def get_value(self) -> Optional[str]:
        return self.element.get_attribute("value", timeout=2)
