from selenium.common.exceptions import NoSuchElementException


class WebElementWrapper:
    def __init__(self, driver, locator: tuple):
        self.driver = driver
        self.locator = locator

    def _get_element(self):
        try:
            return self.driver.find_element(*self.locator)
        except NoSuchElementException:
            raise RuntimeError(f"Element not found: {self.locator}")

    def click(self):
        self._get_element().click()

    def type(self, text: str):
        element = self._get_element()
        element.clear()
        element.send_keys(text)

    def get_text(self) -> str:
        return self._get_element().text

    def is_displayed(self) -> bool:
        return self._get_element().is_displayed()
