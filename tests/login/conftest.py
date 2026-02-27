import pytest

from tests.helpers import PageFixtures


@pytest.fixture
def login_page(driver):
    return PageFixtures.open_login_page(driver)
