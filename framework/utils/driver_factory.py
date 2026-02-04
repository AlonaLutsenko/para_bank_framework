import os

from selenium import webdriver

from framework.utils.appsettings import get_profile, get_setting


class DriverFactory:
    @staticmethod
    def create_driver(browser_name: str = "chrome", headless: bool = None):
        """
        Create a webdriver instance for the specified browser.

        Args:
            browser_name: Name of the browser ('chrome' or 'firefox')
            headless: Whether to run in headless mode. If None, auto-detects from CI environment.
        """
        # Auto-detect headless mode from settings/CI if not explicitly set
        if headless is None:
            is_ci = os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true"
            profile = get_profile("ci" if is_ci else "local")
            headless = profile.get("headless", True if is_ci else False)

        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()

            # Use custom Chrome binary if specified (e.g., chromium-browser in CI)
            chrome_bin = os.getenv("CHROME_BIN")
            if chrome_bin:
                options.binary_location = chrome_bin

            if headless:
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
            else:
                options.add_argument("--start-maximized")

            for arg in get_setting("chrome", "args", default=[]):
                options.add_argument(arg)

            remote_url = os.getenv("SELENIUM_REMOTE_URL")
            if remote_url:
                return webdriver.Remote(command_executor=remote_url, options=options)

            # Use custom ChromeDriver path if specified
            chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
            if chromedriver_path:
                from selenium.webdriver.chrome.service import Service

                service = Service(chromedriver_path)
                return webdriver.Chrome(service=service, options=options)

            return webdriver.Chrome(options=options)

        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Browser '{browser_name}' is not supported")
