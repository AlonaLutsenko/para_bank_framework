class WebDriverWrapper:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        self.driver.get(url)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def quit(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
