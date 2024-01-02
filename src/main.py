from src.framework.server.domain import Request, FirstLine, Headers
from src.framework.server.socket import Socket


def main():
    sock = Socket()
    sock.connect("www.python.org", 443)
    sock.encrypt("www.python.org")

    request = Request(
        first_line=FirstLine(
            method="GET",
            path="/",
            protocol="HTTP/1.1",
        ),
        headers=Headers(host="www.python.org"),
    )
    sock.send(request)

    response = sock.receive()

    print(response)


if __name__ == "__main__":
    main()
