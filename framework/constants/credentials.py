from framework.utils.appsettings import get_setting

CREDENTIALS = get_setting(
    "credentials",
    default={
        "default": {"username": "john", "password": "demo"},
        "admin": {"username": "admin_user", "password": "admin_pass"},
        "guest": {"username": "guest_user", "password": "guest_pass"},
    },
)
