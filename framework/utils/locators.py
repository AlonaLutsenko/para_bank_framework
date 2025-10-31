from selenium.webdriver.common.by import By


class Locator:
    def __init__(self, by: By, value: str):
        self.by = by
        self.value = value

    def as_tuple(self):
        return self.by, self.value

    @staticmethod
    def name(locator_str: str):
        return Locator(By.NAME, locator_str)

    @staticmethod
    def css(locator_str: str):
        return Locator(By.CSS_SELECTOR, locator_str)

    @staticmethod
    def xpath(locator_str: str):
        return Locator(By.XPATH, locator_str)

    @staticmethod
    def id(locator_str: str):
        return Locator(By.ID, locator_str)

    @staticmethod
    def class_name(locator_str: str):
        return Locator(By.CLASS_NAME, locator_str)
