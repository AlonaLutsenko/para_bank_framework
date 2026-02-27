from framework.utils.appsettings import get_setting


def get_base_url() -> str:
    """Get base URL from appsettings.json."""
    return get_setting("base_url", default="https://parabank.parasoft.com")
