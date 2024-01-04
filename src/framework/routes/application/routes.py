import functools
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from framework.routes.application.ports import (
    IAnnotationValidator,
    IRouteService,
    Decorator,
)


@dataclass
class RouteService(IRouteService):
    annotation_validator: IAnnotationValidator

    def get_route(self) -> Decorator:
        """
        Factory method
        """

        def _route(*_, **__) -> Callable:
            """Route decorator for Web"""

            def wrapper(func) -> Callable:
                @functools.wraps(func)
                def inner(*args, **kwargs) -> Any:
                    validator = self.annotation_validator
                    errors = validator.validate(func, args, kwargs)

                    if errors:
                        return errors

                    return func(*args, **kwargs)

                return inner

            return wrapper

        return _route
