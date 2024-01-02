import abc
from typing import Protocol

from src.framework.browser.domain import Request


class IBrowser(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def _can_make_protocol(url: str) -> bool:
        ...

    @abc.abstractmethod
    def get(self, url: str):
        ...

    @abc.abstractmethod
    def post(self, url: str, data: dict | None = None):
        ...


class IRequestBuilder(abc.ABC):
    @abc.abstractmethod
    def set_method(self, method: str):
        ...

    @abc.abstractmethod
    def set_path(self, path: str):
        ...

    @abc.abstractmethod
    def set_protocol(self, protocol: str):
        ...

    @abc.abstractmethod
    def add_header(self, **kwargs):
        ...

    @abc.abstractmethod
    def build(self) -> Request:
        ...


class IRequestFactory(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def get_request() -> Request:
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
