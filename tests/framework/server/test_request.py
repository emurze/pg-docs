from framework.web.domain.entities import Request


def test_request() -> None:
    request = Request(
        method='GET',
        path='/',
        protocol='HTTP/1.1',
        headers={'host': 'LERKA'},
    )
    print(request)
