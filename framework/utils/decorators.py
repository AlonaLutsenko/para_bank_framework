import time


# TODO: add logger later
def return_on_exception(exceptions, logger=None, message="", timeout=5, retry_in=5):
    """
    :param exceptions: list. Element: exception object
    :param logger: The logger object to use for logging. Each file has its own logger instance
    :param message: str. Custom exception message
    :param timeout: int (applied if 'timeout' is not passed in kwargs)
    :param retry_in: int (seconds between retries)
    :return:
    """

    def wrapper(decorated_func):
        def inner(*args, **kwargs):
            error = None
            for _ in range(timeout):
                try:
                    result = decorated_func(*args, **kwargs)
                    # logger.log(
                    #     level="INFO",
                    #     message=f"function called with args {*args, *kwargs}",
                    #     extra={"function_name": decorated_func.__name__}
                    # )
                    return result
                except exceptions as e:
                    error = e
                    # logger.log(
                    #     level="ERROR",
                    #     message=f"Exception <{str(error)}> still occurs: {message}",
                    #     extra={"function_name": decorated_func.__name__},
                    #     exc_info=True
                    # )
                    time.sleep(retry_in)
            assert False, f"Exception <{str(error)}> still occurs: {message}"

        return inner

    return wrapper
