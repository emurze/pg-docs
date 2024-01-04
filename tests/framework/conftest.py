import pytest
from project import FastAPI

from src.framework.container import FirstAPI


def get_fastapi_app() -> FastAPI:
    app = FastAPI()
    return app


def get_firstapi_app() -> FirstAPI:
    app = FirstAPI()
    return app


parametrize_two_apps = pytest.mark.parametrize(
    "app",
    (
        get_fastapi_app(),
        get_firstapi_app(),
    ),
)


@pytest.fixture
def fastapi_app() -> FastAPI:
    return get_fastapi_app()


@pytest.fixture
def firstapi_app() -> FirstAPI:
    return get_firstapi_app()
