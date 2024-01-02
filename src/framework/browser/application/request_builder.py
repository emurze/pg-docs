from src.framework.browser.application.ports import IRequestBuilder
from src.framework.browser.domain import Request, Headers, FirstLine


class EmptyFirstLineFactory:
    @staticmethod
    def get() -> FirstLine:
        return FirstLine(method="", path="", protocol="")


class RequestBuilder(IRequestBuilder):
    headers: dict = {}
    body: dict = {}

    def __init__(self, first_line: FirstLine = EmptyFirstLineFactory.get()):
        self.first_line = first_line

    def set_method(self, method: str) -> None:
        self.first_line.method = method

    def set_path(self, path: str) -> None:
        self.first_line.path = path

    def set_protocol(self, protocol: str) -> None:
        self.first_line.protocol = protocol

    def add_header(self, **kwargs) -> None:
        if len(kwargs) > 1:
            raise ValueError("func requires only 1 keyword argument")
        self.headers |= kwargs

    def add_body(self, data: dict) -> None:
        self.body = data

    def build(self) -> Request:
        return Request(
            first_line=self.first_line,
            headers=Headers(**self.headers),
            body=self.body,
        )
