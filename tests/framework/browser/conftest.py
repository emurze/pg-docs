import pytest

from src.framework.web.infrastructure.factories import BrowserFactory


@pytest.fixture
def browser():
    return BrowserFactory.get_browser()
