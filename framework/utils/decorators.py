import functools
import time
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def return_on_timeout(
    default: Any,
    max_attempts: int = 5,
    sleep_time: int = 1,
) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = max(1, max_attempts)
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == attempts - 1:
                        return default
                    time.sleep(sleep_time)

        return wrapper

    return decorator
