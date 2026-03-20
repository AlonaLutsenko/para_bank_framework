from typing import Dict

from framework.utils.appsettings import get_setting

_DEFAULT_CREDENTIALS = {
    "default": {"username": "john", "password": "demo"},
    "admin": {"username": "admin_user", "password": "admin_pass"},
    "guest": {"username": "guest_user", "password": "guest_pass"},
}


def get_credentials(user_type: str = "default") -> Dict[str, str]:
    """Get credentials for the given user type from appsettings.json."""
    credentials = get_setting("credentials", default=_DEFAULT_CREDENTIALS)
    if user_type not in credentials:
        raise ValueError(f"Unknown user_type: '{user_type}'. Available: {list(credentials.keys())}")
    return credentials[user_type]
