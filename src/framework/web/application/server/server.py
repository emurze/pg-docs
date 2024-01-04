from dataclasses import dataclass

from framework.web.application.ports import IServer, ISocket


@dataclass
class Server(IServer):
    socket: ISocket

    def run(
        self,
        port: int,
        host: str | None = None,
        client_amount: int | None = None,
    ) -> None:
        self.socket.bind(host, port)
        self.socket.listen(client_amount)

        while True:
            sock, address = self.socket.accept()

            # sock.encrypt()

            while True:
                request = sock.receive()

                if not request:
                    break
                else:
                    sock.send('Hello world')
