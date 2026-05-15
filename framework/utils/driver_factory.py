import os
from typing import Callable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from framework.run_config import RunConfig


# TODO: add create_remote_chrome
def _create_chrome_driver(headless: bool):
    options = webdriver.ChromeOptions()

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

    if RunConfig.remote():
        remote_url = os.getenv("SELENIUM_REMOTE_URL")
        if remote_url:
            return webdriver.Remote(command_executor=remote_url, options=options)

    service = Service(os.getenv("CHROMEDRIVER_PATH"))
    return webdriver.Chrome(service=service, options=options)


def _create_firefox_driver(headless: bool):
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument("--headless")
    return webdriver.Firefox(options=options)


class DriverFactory:
    _registry: dict[str, Callable[[bool], webdriver.Remote]] = {
        "chrome": _create_chrome_driver,
        "firefox": _create_firefox_driver,
    }

    @classmethod
    def create_driver(cls, browser_name: None, headless: bool | None = None):
        key = browser_name if browser_name else RunConfig.browser()
        headless = headless if headless else RunConfig.headless()

        if key not in cls._registry:
            supported = ", ".join(sorted(cls._registry))
            raise ValueError(f"Browser '{browser_name}' is not supported. Supported: {supported}")

        return cls._registry[key](headless)
