from collections.abc import Callable
from dataclasses import dataclass

from src.framework.routes.application.ports import IRouteService
from src.framework.routes.application.routes import DefaultRouteService
from src.framework.routes.validator import DefaultAnnotationValidator


@dataclass
class AppContainer:
    route_service: IRouteService = DefaultRouteService.get_route(
        DefaultAnnotationValidator()
    )

    def get(self, *args, **kwargs) -> Callable:
        return self.route_service.get_route(*args, **kwargs)

    def post(self, *args, **kwargs) -> Callable:
        return self.route_service.get_route(*args, **kwargs)
