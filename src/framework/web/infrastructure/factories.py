from framework.web.application.browser.connection_runner import \
    ConnectionRunner
from framework.web.application.builders.request_builder import RequestBuilder
from framework.web.application.ports import IBrowser, IServer
from framework.web.application.browser.browser import Browser
from framework.web.application.server.server import Server
from framework.web.infrastructure.connections import (
    NoSecureConnection,
    SecureConnection,
)
from framework.web.infrastructure.socket import Socket


class BrowserFactory:
    @staticmethod
    def get_browser() -> IBrowser:
        socket = Socket()
        return Browser(
            socket=socket,
            request_builder=RequestBuilder(),
            conn=ConnectionRunner(
                socket=socket,
                connections=[
                    SecureConnection(),
                    NoSecureConnection(),
                ]
            ),
        )


class NoSecureBrowserFactory:
    @staticmethod
    def get_browser() -> IBrowser:
        socket = Socket()
        return Browser(
            socket=socket,
            request_builder=RequestBuilder(),
            conn=ConnectionRunner(
                socket=socket,
                connections=[
                    NoSecureConnection(),
                    SecureConnection(),
                ]
            ),
        )


class ServerFactory:
    @staticmethod
    def get_server() -> IServer:
        return Server(socket=Socket())
