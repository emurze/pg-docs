from dataclasses import dataclass
from typing import NoReturn

from src.framework.browser.application.exceptions import ConnectionNotFoundError
from src.framework.browser.application.ports import (
    ISocket,
    IConnection,
    IBrowser,
    IRequestBuilder,
)


@dataclass
class Browser(IBrowser):
    socket: ISocket
    request_builder: IRequestBuilder
    connections: list[IConnection]  # First connection is default connection

    @staticmethod
    def _can_make_protocol(url: str) -> bool:
        return bool(~url.find("://"))

    def _make_default_connection(self) -> IConnection | NoReturn:
        try:
            return self.connections[0]
        except KeyError:
            raise ConnectionNotFoundError(
                "Please specify at least 1 connection",
            )

    def _make_protocol_and_host(self, url: str) -> list[str]:
        if self._can_make_protocol(url):
            return url.split("://")
        else:
            default_connection = self._make_default_connection()
            return [default_connection.protocol, url]

    @staticmethod
    def _make_conn(conns: list[IConnection], protocol: str) -> IConnection:
        conns_dict = {conn.protocol: conn for conn in conns}
        return conns_dict.get(protocol)

    def get(self, url: str) -> str:
        protocol, host = self._make_protocol_and_host(url)

        connection = self._make_conn(self.connections, protocol)
        connection.connect(self.socket, host)

        builder = self.request_builder
        builder.set_method("GET")
        builder.set_path("/")
        builder.set_protocol("HTTP/1.1")
        builder.add_header(host=host)
        request = builder.build()

        self.socket.send(request)
        response = self.socket.receive()
        return response

    def post(self, url: str, data: dict | None = None):
        pass
