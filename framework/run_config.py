class RunConfig:
    __base_url = None
    __browser = None
    __headless = None
    __remote = None

    @staticmethod
    def base_url():
        return RunConfig.__base_url

    @staticmethod
    def __set_base_url(url):
        RunConfig.__base_url = url

    @staticmethod
    def browser():
        return RunConfig.__browser

    @staticmethod
    def __set_browser(browser):
        RunConfig.__browser = browser

    @staticmethod
    def headless():
        return RunConfig.__headless

    @staticmethod
    def __set_headless(headless: bool):
        RunConfig.__headless = headless

    @staticmethod
    def remote():
        return RunConfig.__remote

    @staticmethod
    def __set_remote(remote: bool):
        RunConfig.__remote = remote

    @staticmethod
    def set_run_config(**kwargs):
        RunConfig.__set_base_url(kwargs.get("base_url"))
        RunConfig.__set_browser(kwargs.get("browser"))
        RunConfig.__set_headless(kwargs.get("headless"))
        RunConfig.__set_remote(kwargs.get("remote"))
