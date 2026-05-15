from contextlib import contextmanager
from typing import Callable

import allure


class AllureHelper:
    @staticmethod
    def case(epic: str, feature: str, story: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            wrapped = allure.story(story)(func)
            wrapped = allure.feature(feature)(wrapped)
            wrapped = allure.epic(epic)(wrapped)
            return wrapped

        return decorator

    @staticmethod
    @contextmanager
    def step(title: str):
        with allure.step(title):
            yield


def case(epic: str, feature: str, story: str) -> Callable:
    return AllureHelper.case(epic, feature, story)


@contextmanager
def step(title: str):
    with AllureHelper.step(title):
        yield
