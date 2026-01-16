import os

from selenium import webdriver


class DriverFactory:
    @staticmethod
    def create_driver(browser_name: str = "chrome", headless: bool = None):
        """
        Create a webdriver instance for the specified browser.

        Args:
            browser_name: Name of the browser ('chrome' or 'firefox')
            headless: Whether to run in headless mode. If None, auto-detects from CI environment.
        """
        # Auto-detect headless mode from CI environment if not explicitly set
        if headless is None:
            headless = os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true"

        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
            else:
                options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)

        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Browser '{browser_name}' is not supported")
