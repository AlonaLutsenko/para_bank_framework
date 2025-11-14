from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    @staticmethod
    def create_driver(browser_name: str = "chrome"):
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            service = webdriver.chrome.service.Service(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)

        elif browser_name.lower() == "firefox":
            service = webdriver.firefox.service.Service(GeckoDriverManager().install())
            return webdriver.Firefox(service=service)

        else:
            raise ValueError(f"Browser '{browser_name}' is not supported")
