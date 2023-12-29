import pytest

from src.billy_shop.domain import User


@pytest.fixture
def user():
    return User(id=1)
