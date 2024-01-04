from framework.web.domain.entities import Request


class EmptyRequestFactory:
    """Domain Service Factory for Request"""

    @staticmethod
    def get() -> Request:
        return Request(
            method="",
            path="",
            protocol="",
            headers={},
        )
