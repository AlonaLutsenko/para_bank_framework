import os
from pathlib import Path
from typing import Dict

from dotenv import load_dotenv

# Load .env from project root (parent of framework/)
_env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(_env_path)

# Supported user types and their env var suffixes
_USER_TYPES = ("default", "admin", "guest")
_ENV_USER = "PARABANK_USERNAME_{}"
_ENV_PASS = "PARABANK_PASSWORD_{}"


def _credentials_from_env() -> Dict[str, Dict[str, str]]:
    creds = {}
    for user_type in _USER_TYPES:
        suffix = user_type.upper()
        username = os.getenv(_ENV_USER.format(suffix))
        password = os.getenv(_ENV_PASS.format(suffix))
        if username and password:
            creds[user_type] = {"username": username, "password": password}
    return creds


def get_credentials(user_type: str = "default") -> Dict[str, str]:
    env_creds = _credentials_from_env()
    if user_type in env_creds:
        return env_creds[user_type]

    if env_creds:
        raise ValueError(
            f"Unknown user_type: '{user_type}'. "
            f"Available: {list(env_creds.keys())}. "
            f"Set PARABANK_USERNAME_{user_type.upper()} and PARABANK_PASSWORD_{user_type.upper()}."
        )

    raise ValueError(
        f"No credentials found for '{user_type}'. "
        "Set PARABANK_USERNAME_DEFAULT and PARABANK_PASSWORD_DEFAULT in .env, "
        "or add them as GitHub Secrets for CI."
    )
