from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver


class DriverFactory:
    @staticmethod
    def create_driver(browser_name: str = "chrome"):
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(ChromeDriverManager().install(), options=options)  # noqa: E501

        elif browser_name.lower() == "firefox":
            return webdriver.Firefox(GeckoDriverManager().install())

        else:
            raise ValueError(f"Browser '{browser_name}' is not supported")
