from src.framework.browser.application.ports import IBrowser
from src.framework.browser.application.browser import Browser
from src.framework.browser.application.request_builder import RequestBuilder
from src.framework.browser.infrastructure.connections import (
    NoSecureConnection,
    SecureConnection,
)
from src.framework.browser.infrastructure.socket import Socket


class BrowserFactory:
    @staticmethod
    def get_browser() -> IBrowser:
        return Browser(
            socket=Socket(),
            request_builder=RequestBuilder(),
            connections=[
                SecureConnection(),
                NoSecureConnection(),
            ],
        )
