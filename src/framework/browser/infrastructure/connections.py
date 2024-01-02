from src.framework.browser.application.ports import IConnection, ISocket


class NoSecureConnection(IConnection):
    protocol: str = "http"
    port: int = 80

    def connect(self, socket: ISocket, host: str) -> None:
        socket.connect(host, self.port)


class SecureConnection(IConnection):
    protocol: str = "https"
    port: int = 443

    def connect(self, socket: ISocket, host: str) -> None:
        socket.connect(host, self.port)
        socket.encrypt(host)
