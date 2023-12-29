import functools
from collections.abc import Callable
from typing import Any

from src.framework.routes.application.ports import (
    IAnnotationValidator,
    IRouteService,
)


class DefaultRouteService(IRouteService):
    @staticmethod
    def get_route(annotation_validator: IAnnotationValidator):
        """
        Factory method
        """

        def _route(*_, **__) -> Callable:
            """Route decorator for Web"""
            ant_validator = annotation_validator

            def wrapper(func) -> Callable:
                @functools.wraps(func)
                def inner(*args, **kwargs) -> Any:
                    validated_data = ant_validator.validate(func, args, kwargs)

                    if errors := validated_data.errors:
                        return {"errors": errors}

                    return func(*validated_data.args, **validated_data.kwargs)

                return inner

            return wrapper

        return _route
