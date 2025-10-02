from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:
    @staticmethod
    def create_driver(browser_name: str = "chrome"):
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        elif browser_name.lower() == "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        else:
            raise ValueError(f"Browser f'{browser_name}' is not supported")