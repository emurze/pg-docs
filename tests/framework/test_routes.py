from src.billy_shop.domain import User
from src.framework.routes.application.ports import Decorator


def test_get_route_base_model_success(route: Decorator, user: User) -> None:
    @route("/")
    def some_func(param1: int, some_user: User) -> dict:
        return {
            "param1": param1,
            "user_id": some_user.id,
        }

    assert some_func(1, some_user=user)


def test_get_route_dict_success(route: Decorator) -> None:
    user_dict = {
        "id": 1,
    }

    @route("/")
    def some_func(param1: int, some_user: User) -> dict:
        return {
            "param1": param1,
            "user_id": some_user.id,
        }

    assert some_func(1, some_user=user_dict)
