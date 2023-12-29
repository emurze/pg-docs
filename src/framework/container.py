from collections.abc import Callable

from src.framework.router import route


class AppContainer:
    @staticmethod
    def get(*args, **kwargs) -> Callable:
        return route(*args, **kwargs)

    @staticmethod
    def post(*args, **kwargs) -> Callable:
        return route(*args, **kwargs)

    @staticmethod
    def put(*args, **kwargs) -> Callable:
        return route(*args, **kwargs)

    @staticmethod
    def patch(*args, **kwargs) -> Callable:
        return route(*args, **kwargs)
