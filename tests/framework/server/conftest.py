import pytest

from src.framework.server.server import (
    Browser,
    DefaultConnection,
    SecureConnection
)
from src.framework.server.socket import Socket


@pytest.fixture
def browser():
    return Browser(
        Socket(),
        [DefaultConnection(), SecureConnection()],
    )
