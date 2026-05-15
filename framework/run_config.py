class RunConfig:
    __base_url = None

    @staticmethod
    def base_url():
        return RunConfig.__base_url

    @staticmethod
    def set_base_url(url: str) -> None:
        RunConfig.__base_url = url
