from framework.utils.wait import Wait


class BasePage:
    def __init__(self, driver, wait_timeout: int = 10):
        self.driver = driver
        self.wait = Wait(driver, timeout=wait_timeout)

    def open(self, url):
        self.driver.get(url)
        self.wait.with_custom_condition(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
