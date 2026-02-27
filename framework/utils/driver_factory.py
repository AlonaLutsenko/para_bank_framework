import os
from typing import Callable

from selenium import webdriver

from framework.utils.appsettings import get_profile, get_setting


def _resolve_headless(headless: bool | None) -> bool:
    if headless is not None:
        return headless
    is_ci = os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true"
    profile = get_profile("ci" if is_ci else "local")
    return profile.get("headless", True if is_ci else False)


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

    for arg in get_setting("chrome", "args", default=[]):
        options.add_argument(arg)

    remote_url = os.getenv("SELENIUM_REMOTE_URL")
    if remote_url:
        return webdriver.Remote(command_executor=remote_url, options=options)

    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
    if chromedriver_path:
        from selenium.webdriver.chrome.service import Service

        service = Service(chromedriver_path)
        return webdriver.Chrome(service=service, options=options)

    return webdriver.Chrome(options=options)


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
    def register(cls, browser_name: str) -> Callable:
        def decorator(creator: Callable[[bool], webdriver.Remote]):
            cls._registry[browser_name.lower()] = creator
            return creator

        return decorator

    @classmethod
    def create_driver(cls, browser_name: str = "chrome", headless: bool | None = None):
        headless = _resolve_headless(headless)
        key = browser_name.lower()

        if key not in cls._registry:
            supported = ", ".join(sorted(cls._registry))
            raise ValueError(f"Browser '{browser_name}' is not supported. Supported: {supported}")

        return cls._registry[key](headless)
