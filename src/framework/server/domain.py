from typing import Literal, ClassVar

from pydantic import BaseModel

Method = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]


class FirstLine(BaseModel):
    method: Method
    path: str
    protocol: str

    def __str__(self) -> str:
        return f"{self.method} {self.path} {self.protocol}"


class Headers(BaseModel):
    host: str

    def __str__(self) -> str:
        return f"Host: {self.host}"


class Request(BaseModel):
    first_line: FirstLine
    headers: Headers
    body: dict | None = None
    sep: ClassVar[str] = "\r\n"

    def __str__(self) -> str:
        fields = [
            self.first_line,
            self.headers,
        ]

        if self.body:
            fields.append(self.body)

        return f"{self.sep.join(map(str, fields))}{self.sep * 2}"

    def encode(self) -> bytes:
        return str(self).encode()
