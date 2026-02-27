import functools
from typing import Any, Callable, TypeVar

from selenium.common.exceptions import TimeoutException

F = TypeVar("F", bound=Callable[..., Any])


def return_on_timeout(default: Any) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except TimeoutException:
                return default

        return wrapper

    return decorator
