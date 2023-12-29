import abc
from collections.abc import Callable
from typing import Any, NewType

from src.framework.routes.application.dto import ValidatedDTO


Decorator = NewType("Decorator", Callable)  # type: ignore


class IAnnotationValidator(abc.ABC):
    """
    Method validate() should return list of errors
    """

    @abc.abstractmethod
    def validate(self, func: Callable, args: Any, kwargs: Any) -> ValidatedDTO:
        ...


class IRouteService(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def get_route(annotation_validator: IAnnotationValidator) -> Decorator:
        """This factory method returns route decorator"""
