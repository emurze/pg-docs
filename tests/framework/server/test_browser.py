from src.framework.browser.application.ports import IBrowser
from src.framework.browser.domain import Headers, Request, FirstLine
from src.framework.browser.infrastructure.socket import Socket


def test_socket() -> None:
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


def test_can_make_protocol(browser: IBrowser) -> None:
    res = browser._can_make_protocol("https://hi.com")
    assert res is True


def test_can_make_protocol_failure(browser: IBrowser) -> None:
    res = browser._can_make_protocol("www.hi.com")
    assert res is False


def test_browser_get(browser: IBrowser):
    pr = browser.get("github.com")

    print(pr)
