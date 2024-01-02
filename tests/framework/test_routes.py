from typing import Any

import pytest
from pydantic import BaseModel
from tests.framework.conftest import parametrize_two_apps


class Trade(BaseModel):
    id: int
    price: float


success_trade = {"id": 23, "price": 1.335}
failure_trade = {"id": 12, "price": "ef"}


@parametrize_two_apps
@pytest.mark.parametrize(
    "new_trade", ({"id": 23, "price": 1.335}, {"id": 12, "price": "ef"})
)
def test_trade_validation_success(app: Any, new_trade: dict) -> None:
    @app.get("/")
    def some_func(trade: Trade) -> dict:
        return {"id": trade["id"], "price": trade["price"]}

    response = some_func(trade=new_trade)  # noqa
