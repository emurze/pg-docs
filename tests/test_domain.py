import pytest
from pydantic import ValidationError

from src.billy_shop.domain import User


@pytest.mark.parametrize(
    "kwargs",
    (
        {
            "id": 1,
            "name": 35,
        },
        {
            "id": 1,
            "friends": {"1": "2"},
        },
        {
            "id": 1,
            "sign_up": "string",
        },
    ),
)
def test_user_validation_errors(kwargs: dict) -> None:
    with pytest.raises(ValidationError):
        User(**kwargs)


def test_can_create_user() -> None:
    user = User(id=1)
    assert user.id == 1
    assert user.name == "Vlad"
    assert user.sign_up is None
    assert user.friends == []
