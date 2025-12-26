from framework.utils.wait import Wait
from framework.utils.wait_conditions import WaitConditions
from framework.utils.web_driver_wrapper import WebDriverWrapper


class BasePage:
    def __init__(self, driver: WebDriverWrapper, wait_timeout: int = 10):
        self.driver = driver
        self.wait = Wait(driver, timeout=wait_timeout)

    def open(self, url):
        self.driver.open(url)
        self.wait.with_custom_condition(WaitConditions.page_load_complete())
