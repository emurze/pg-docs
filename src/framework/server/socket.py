import socket
import ssl
from dataclasses import dataclass

from src.framework.server.domain import Request
from src.framework.server.ports import ISocket


@dataclass(frozen=True)
class INET:
    ip4: int = socket.AF_INET
    ip6: int = socket.AF_INET6


@dataclass(frozen=True)
class Connection:
    TCP: int = socket.SOCK_STREAM
    UDP: int = socket.SOCK_DGRAM


class Socket(ISocket):
    def __init__(
        self, inet: int = INET.ip4, conn: int = Connection.TCP
    ) -> None:
        self.socket = socket.socket(inet, conn)

    def connect(self, host: str, port: int) -> None:
        self.socket.connect((host, port))

    def encrypt(self, hostname: str) -> None:
        context = ssl.create_default_context()
        self.socket = context.wrap_socket(
            self.socket, server_hostname=hostname
        )

    def send(self, request: Request) -> None:
        self.socket.sendall(request.encode())

    def receive(self, batch: int = 1024) -> str:
        response = self.socket.recv(batch)
        return response.decode()

    def close(self) -> None:
        self.socket.close()
