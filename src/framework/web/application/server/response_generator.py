from framework.web.application.ports import IResponseGenerator
from framework.web.domain.entities import Request


class ResponseGenerator(IResponseGenerator):
    def generate(self, request: Request):
        pass
