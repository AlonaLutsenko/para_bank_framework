from framework.utils.wait import Wait
from framework.utils.web_driver_wrapper import WebDriverWrapper


class BasePage:
    def __init__(self, driver: WebDriverWrapper, wait_timeout: int = 10):
        self.driver = driver
        self.wait = Wait(driver.driver, timeout=wait_timeout)

    def open(self, url):
        self.driver.open(url)
        self.wait.with_custom_condition(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
