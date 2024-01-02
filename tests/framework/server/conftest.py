import pytest

from src.framework.browser.infrastructure.factory import BrowserFactory


@pytest.fixture
def browser():
    return BrowserFactory.get_browser()
