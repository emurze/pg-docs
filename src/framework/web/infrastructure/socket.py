import socket
import ssl
from dataclasses import dataclass

from framework.web.application.ports import ISocket

DEFAULT_SERVER_PORT = 3000
DEFAULT_SERVER_HOST = "127.0.0.1"
DEFAULT_MAX_CLIENT_AMOUNT = 5


@dataclass(frozen=True)
class INET:
    ip4: int = socket.AF_INET
    ip6: int = socket.AF_INET6


@dataclass(frozen=True)
class Connection:
    TCP: int = socket.SOCK_STREAM
    UDP: int = socket.SOCK_DGRAM


class Socket(ISocket):
    def __init__(self, new_socket: socket.socket | None = None) -> None:
        if new_socket is None:
            self.socket = socket.socket(INET.ip4, Connection.TCP)
        else:
            self.socket = new_socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def connect(self, host: str, port: int) -> None:
        self.socket.connect((host, port))

    def encrypt(self, hostname: str) -> None:
        context = ssl.create_default_context()
        self.socket = context.wrap_socket(
            self.socket, server_hostname=hostname
        )

    def encrypt_server(self, certfile: str, keyfile: str) -> None:
        self.socket = ssl.wrap_socket(
            self.socket,
            server_side=True,
            certfile=certfile,
            keyfile=keyfile,
        )

    def send(self, message: str, batch: int = 1024) -> None:
        self.socket.sendall(message.encode())

    def receive(self, batch: int = 1024) -> str:
        response = self.socket.recv(batch)
        return response.decode()

    def bind(
        self,
        host: str = DEFAULT_SERVER_HOST,
        port: int = DEFAULT_SERVER_PORT,
    ) -> None:
        self.socket.bind((host, port))

    def listen(self, client_amount: int = DEFAULT_MAX_CLIENT_AMOUNT) -> None:
        self.socket.listen(client_amount)

    def accept(self) -> tuple['ISocket', tuple]:
        client_socket, address = self.socket.accept()
        return Socket(client_socket), address

    def close_connection(self) -> None:
        self.socket.close()
        self.socket = socket.socket(self.socket.family, self.socket.type)
