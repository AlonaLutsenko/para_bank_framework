from selenium.common.exceptions import TimeoutException


class WebDriverWrapper:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        try:
            self.driver.get(url)
        except TimeoutException:
            raise RuntimeError(f"Page load timeout: {url}")
