# framework/utils/webdriver_wrapper.py
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By


class WebDriverWrapper:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        try:
            self.driver.get(url)
        except TimeoutException:
            raise RuntimeError(f"Page load timeout: {url}")

    def find(self, locator: tuple[By, str]):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            raise RuntimeError(f"Element not found: {locator}")

    def click(self, locator: tuple[By, str]):
        element = self.find(locator)
        element.click()

    def type(self, locator: tuple[By, str], text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
