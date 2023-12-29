from collections.abc import Iterator

from pydantic import BaseModel


class ValidatedDTO(BaseModel):
    args: list = []
    kwargs: dict = {}
    errors: list = []
