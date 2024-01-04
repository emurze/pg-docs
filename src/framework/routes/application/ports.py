import abc
from collections.abc import Callable
from typing import Any, NewType, Protocol

from framework.routes.application.dto import ValidatedDTO


Decorator = NewType("Decorator", Callable)  # type: ignore


class IAnnotationValidator(abc.ABC):
    """
    Method validate() should return list of errors
    """

    @abc.abstractmethod
    def validate(self, func: Callable, args: Any, kwargs: Any) -> ValidatedDTO:
        ...


class IRouteService(Protocol):
    annotation_validator: IAnnotationValidator

    @abc.abstractmethod
    def get_route(self) -> Decorator:
        """This factory method returns route decorator"""
