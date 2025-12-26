from selenium import webdriver


class DriverFactory:
    @staticmethod
    def create_driver(browser_name: str = "chrome"):
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)

        elif browser_name.lower() == "firefox":
            return webdriver.Firefox()

        else:
            raise ValueError(f"Browser '{browser_name}' is not supported")
