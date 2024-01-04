import abc
from typing import Protocol, Callable

from framework.web.domain.entities import Request


class IBrowser(abc.ABC):
    @abc.abstractmethod
    def get(self, url: str, port: int | None = None):
        ...

    @abc.abstractmethod
    def post(
        self,
        url: str,
        data: dict | None = None,
        port: int | None = None,
    ):
        ...


class IServer(abc.ABC):
    @abc.abstractmethod
    def run(self, host: str, port: int, client_amount: int) -> None: ...



class IRequestBuilder(abc.ABC):
    @abc.abstractmethod
    def set_method(self, method: str) -> None:
        ...

    @abc.abstractmethod
    def set_path(self, path: str) -> None:
        ...

    @abc.abstractmethod
    def set_protocol(self, protocol: str):
        ...

    @abc.abstractmethod
    def add_header(self, **kwargs) -> None:
        ...

    @abc.abstractmethod
    def add_body(self, data: dict) -> None:
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
    def send(self, message: str) -> str:
        ...

    @abc.abstractmethod
    def encrypt(self, hostname: str) -> None:
        ...

    @abc.abstractmethod
    def receive(self) -> str:
        ...

    @abc.abstractmethod
    def bind(self, host: str, port: int) -> None: ...

    @abc.abstractmethod
    def listen(self, client_amount: int) -> None: ...

    @abc.abstractmethod
    def accept(self) -> tuple['ISocket', tuple]: ...

    @abc.abstractmethod
    def close_connection(self) -> None:
        ...


class IConnection(Protocol):
    protocol: str

    @abc.abstractmethod
    def connect(self, socket: ISocket, host: str, new_port: int = 0) -> None:
        ...


class IConnectionRunner(Protocol):
    connections: list[IConnection]
    host: str | None = None

    @staticmethod
    @abc.abstractmethod
    def connect_methods(other) -> None: ...

    @abc.abstractmethod
    def connect(self, func: Callable) -> Callable: ...


class IResponseGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self, request: Request): ...
