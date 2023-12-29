from datetime import date

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "Vlad"
    sign_up: date | None = None
    friends: list[int] = []
