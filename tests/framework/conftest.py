import pytest

from src.framework.routes.application.ports import (
    IAnnotationValidator,
    IRouteService,
    Decorator,
)
from src.framework.routes.application.routes import DefaultRouteService
from src.framework.routes.validator import DefaultAnnotationValidator


@pytest.fixture
def annotation_validator() -> IAnnotationValidator:
    return DefaultAnnotationValidator()


@pytest.fixture
def route_service() -> IRouteService:
    return DefaultRouteService()


@pytest.fixture
def route(annotation_validator, route_service) -> Decorator:
    return DefaultRouteService.get_route(annotation_validator)
