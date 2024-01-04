import pytest

from src.framework.web.application.ports import IServer
from src.framework.web.infrastructure.factories import ServerFactory


@pytest.fixture
def server() -> IServer:
    return ServerFactory.get_server()
