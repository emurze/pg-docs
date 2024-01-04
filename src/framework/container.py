from collections.abc import Callable
from dataclasses import dataclass

from framework.routes.application.ports import IRouteService, Decorator
from framework.routes.application.routes import RouteService
from framework.routes.validator import AnnotationValidator


@dataclass
class FirstAPI:
    route_service: IRouteService = RouteService(AnnotationValidator())
    route: Decorator = route_service.get_route()

    def get(self, *args, **kwargs) -> Callable:
        return self.route(*args, **kwargs)

    def post(self, *args, **kwargs) -> Callable:
        return self.route(*args, **kwargs)
