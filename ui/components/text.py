from typing import Optional

from framework.utils.decorators import return_on_timeout
from framework.utils.locators import Locator
from framework.utils.web_driver_wrapper import WebDriverWrapper
from ui.components.base_component import BaseComponent


class Text(BaseComponent):
    def __init__(self, driver: WebDriverWrapper, locator: Locator):
        super().__init__(driver, locator)

    @return_on_timeout(None)
    def get_text(self) -> Optional[str]:
        return self.element.get_text()
