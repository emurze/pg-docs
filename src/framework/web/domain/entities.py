from pydantic import BaseModel

SEP = "\r\n"


class Request(BaseModel):
    method: str
    path: str
    protocol: str
    headers: dict
    body: dict | None = None

    def deserialize(self):
        pass

    def __str__(self) -> str:
        fields = [
            f'{self.method} {self.path} {self.protocol}',
            SEP.join(
                f'{key.upper()}: {value}'
                for key, value in self.headers.items()
            ),
        ]
        if self.body:
            fields.append(str(self.body))

        return f"{SEP.join(fields)}{SEP * 2}"
