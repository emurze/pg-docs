from framework.web.application.ports import IRequestBuilder
from framework.web.domain.entities import Request
from framework.web.domain.factories import EmptyRequestFactory


class RequestBuilder(IRequestBuilder):
    def __init__(self, request: Request = EmptyRequestFactory.get()):
        self.request = request

    def set_method(self, method: str) -> None:
        self.request.method = method

    def set_path(self, path: str) -> None:
        self.request.path = path

    def set_protocol(self, protocol: str) -> None:
        self.request.protocol = protocol

    def add_header(self, **kwargs) -> None:
        if len(kwargs) > 1:
            raise ValueError("func requires only 1 keyword argument")
        self.request.headers |= kwargs

    def add_body(self, data: dict) -> None:
        self.request.body = data

    def build(self) -> Request:
        return self.request
