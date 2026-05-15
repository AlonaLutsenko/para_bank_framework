import os
from collections.abc import Callable

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


def _remote_session(options: BaseOptions) -> WebDriver:
    remote_url = os.getenv("SELENIUM_REMOTE_URL")
    if not remote_url:
        raise ValueError("SELENIUM_REMOTE_URL is not set.")
    return webdriver.Remote(command_executor=remote_url, options=options)


def _chrome_options(headless: bool, *, remote: bool = False) -> ChromeOptions:
    options = ChromeOptions()

    if headless:
        options.add_argument("--headless")
        if remote:
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
    else:
        options.add_argument("--start-maximized")

    return options


def _firefox_options(headless: bool) -> FirefoxOptions:
    options = FirefoxOptions()

    if headless:
        options.add_argument("-headless")

    return options


def _create_chrome_driver(headless: bool, remote: bool) -> WebDriver:
    options = _chrome_options(headless, remote=remote)
    if remote:
        return _remote_session(options)
    return webdriver.Chrome(options=options)


def _create_firefox_driver(headless: bool, remote: bool) -> WebDriver:
    options = _firefox_options(headless)
    if remote:
        return _remote_session(options)
    return webdriver.Firefox(options=options)


class DriverFactory:
    _registry: dict[str, Callable[[bool, bool], WebDriver]] = {
        "chrome": _create_chrome_driver,
        "firefox": _create_firefox_driver,
    }

    @classmethod
    def create_driver(cls, browser_name: str, *, headless: bool, remote: bool) -> WebDriver:
        if browser_name not in cls._registry:
            raise ValueError(f"Browser '{browser_name}' is not supported.")

        return cls._registry[browser_name](headless, remote)
