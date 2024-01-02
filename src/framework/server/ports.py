import abc
from typing import Protocol

from src.framework.server.domain import Request


class IBrowser(abc.ABC):
    @abc.abstractmethod
    def get(self, url: str):
        ...

    @abc.abstractmethod
    def post(self, url: str, data: dict | None = None):
        ...


class ISocket(abc.ABC):
    @abc.abstractmethod
    def connect(self, host: str, port: int) -> None:
        ...

    @abc.abstractmethod
    def send(self, request: Request) -> None:
        ...

    @abc.abstractmethod
    def encrypt(self, hostname: str) -> None:
        ...

    @abc.abstractmethod
    def receive(self) -> str:
        ...

    @abc.abstractmethod
    def close(self) -> None:
        ...


class IConnection(Protocol):
    protocol: str

    @abc.abstractmethod
    def connect(self, socket: ISocket, host: str) -> None:
        ...
