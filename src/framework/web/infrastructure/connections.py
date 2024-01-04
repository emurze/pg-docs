from framework.web.application.ports import IConnection, ISocket


class NoSecureConnection(IConnection):
    protocol: str = "http"
    port: int = 80

    def connect(self, socket: ISocket, host: str, new_port: int = 0) -> None:
        socket.connect(host, new_port or self.port)


class SecureConnection(IConnection):
    protocol: str = "https"
    port: int = 443

    def connect(self, socket: ISocket, host: str, new_port: int = 0) -> None:
        socket.connect(host, new_port or self.port)
        socket.encrypt(host)
