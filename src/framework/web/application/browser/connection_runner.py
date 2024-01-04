import functools
from dataclasses import dataclass
from typing import NoReturn, Callable, Any

from framework.helpers.get_non_magic_methods import get_non_magic_methods
from framework.web.application.exceptions import ConnectionNotFoundError
from framework.web.application.ports import (
    IConnectionRunner, ISocket, IConnection
)


@dataclass
class ConnectionRunner(IConnectionRunner):
    """
    It is responsible for opening and closing connection automatically.

    You can:
        Wrap each method using @connect
            * It implements opening and closing connection
            * it allows you to use self.conn.host

        Or call this trick, it will wrap each your method using @connect:
            self.connection_runner.connect_methods(self)
    """

    socket: ISocket
    connections: list[IConnection]  # First connection is default
    host: str | None = None

    @staticmethod
    def _can_take_protocol(url: str) -> bool:
        return bool(~url.find("://"))

    @staticmethod
    def _get_default_conn(conns: list[IConnection]) -> IConnection | NoReturn:
        """
        Try to get a first conn item as default connection
        """

        try:
            return conns[0]
        except IndexError:
            raise ConnectionNotFoundError(
                "Please specify at least 1 connection",
            )

    @staticmethod
    def _get_conn(protocol: str, conns: list[IConnection]) -> IConnection:
        """
        Get a connection algorithm depending on the protocol
        Example:
            http -> UnSecured
            https -> Secured
        """

        conns_dict = {conn.protocol: conn for conn in conns}
        return conns_dict.get(protocol)

    def _open_connection(self, url: str, port: int) -> str:
        """
        Open connection depending on url protocol or default algorithm
        return generated host
        """

        if self._can_take_protocol(url):
            protocol, host = url.split("://")
            conn = self._get_conn(protocol, self.connections)
        else:
            host = url
            conn = self._get_default_conn(self.connections)

        conn.connect(self.socket, host, port)
        return host

    def _close_connection(self) -> None:
        self.socket.close_connection()

    def connect(self, func: Callable) -> Callable:
        """
        Decorator to connect and automatically close connection
        """

        @functools.wraps(func)
        def wrapper(*args, url: str = '', port: int = 0, **kwargs) -> Any:
            if args:
                url = args[0]
            if len(args) > 1:
                port = args[1]

            self.host = self._open_connection(url, port)

            res = func(*args, **kwargs)

            self._close_connection()

            return res

        return wrapper

    @staticmethod
    def connect_methods(other) -> None:
        """
        Trick to wrap all class methods using @connect decorator
        """

        methods = get_non_magic_methods(other)
        for method in methods:
            setattr(other, method.__name__, other.conn.connect(method))
