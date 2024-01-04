from dataclasses import dataclass
from framework.web.application.ports import (
    IBrowser, ISocket, IRequestBuilder, IConnectionRunner
)


@dataclass
class Browser(IBrowser):
    socket: ISocket
    request_builder: IRequestBuilder
    conn: IConnectionRunner  # You can use self.conn.host

    def __post_init__(self) -> None:
        self.conn.connect_methods(self)

    def get(self, url: str, port: int = 0) -> str:
        builder = self.request_builder
        builder.set_method("GET")
        builder.set_path("/")
        builder.set_protocol("HTTP/1.1")
        builder.add_header(host=self.conn.host)
        request = builder.build()

        self.socket.send(str(request))
        response = self.socket.receive()
        return response

    def post(self, url: str, port: int = 0, data: dict | None = None):
        builder = self.request_builder
        builder.set_method("POST")
        builder.set_path("/")
        builder.set_protocol("HTTP/1.1")
        builder.add_header(host=self.conn.host)
        builder.add_body(data=data)
        request = builder.build()

        self.socket.send(str(request))
        response = self.socket.receive()
        return response
