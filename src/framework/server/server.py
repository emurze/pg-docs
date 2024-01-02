from dataclasses import dataclass

from src.framework.server.domain import Request, FirstLine, Headers
from src.framework.server.ports import ISocket, IConnection


class SecureConnection(IConnection):
    protocol: str = 'https'
    port: int = 443

    def connect(self, socket: ISocket, host: str) -> None:
        socket.connect(host, self.port)
        socket.encrypt(host)


class DefaultConnection(IConnection):
    protocol: str = 'http'
    port: int = 80

    def connect(self, socket: ISocket, host: str) -> None:
        socket.connect(host, self.port)


@dataclass
class Browser:
    socket: ISocket
    connections: list[IConnection]

    @staticmethod
    def _make_protocol_and_host(url: str) -> list[str]:
        return url.split("://")

    @staticmethod
    def _make_conn(conns: list[IConnection], protocol: str) -> IConnection:
        conns = {conn.protocol: conn for conn in conns}
        return conns.get(protocol)

    def get(self, url: str) -> str:
        protocol, host = self._make_protocol_and_host(url)

        connection = self._make_conn(self.connections, protocol)
        connection.connect(self.socket, host)

        request = Request(
            first_line=FirstLine(
                method="GET",
                path=url,
                protocol="HTTP/1.1",
            ),
            headers=Headers(host=host),
        )

        self.socket.send(request)

        response = self.socket.receive()
        return response


    def post(self, url: str, data: dict | None = None):
        pass
