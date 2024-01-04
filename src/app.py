import enum

from fastapi import FastAPI
from fastapi.exceptions import ResponseValidationError
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI(
    title="Trading App"
)

fake_users = [
    {"id": 1, "name": "Vlad"},
    {"id": 2, "name": "Lera"},
    {"id": 3, "name": "Dzimka"},
]

fake_users2 = [
    {"id": 1, "name": "Vlad"},
    {"id": 2, "name": "Lera"},
    {"id": 3, "name": "Dzimka"},
]

fake_trades = [
    {"id": 1,
     "title": "Trace 1",
     "price": 13.23,
     "statuses": [
        {"id": 1, "type": "monkey"},
        {"id": 1, "type": "success"},
     ]},
]


class StatusType(enum.Enum):
    failure: str = "failure"
    pending: str = "pending"
    success: str = "success"



class Status(BaseModel):
    id: int
    type: StatusType



class Trade(BaseModel):
    id: int
    title: str = Field(min_length=3)
    price: float = Field(ge=0)
    statuses: list[Status] | None = None


@app.get("/users/{user_id}")
def get_user(user_id: int) -> list:
    return [user for user in fake_users if user["id"] == user_id]


@app.get("/trades", response_model=list[Trade])
def get_trades(limit: int = 100, offset: int = 0):
    return fake_trades


@app.patch("/users/{user_id}")
def update_user_name(user_id: int, new_name: str) -> dict:
    user = [user for user in fake_users2 if user["id"] == user_id][0]
    user["name"] = new_name
    return {
        "status": 200,
        "data": user,
    }


@app.post('/trades')
def add_trades(trades: list[Trade]) -> dict:
    fake_trades.extend(trades)
    return {
        'status': 200,
        'data': fake_trades,
    }


@app.exception_handler(ResponseValidationError)
async def validation_exception_error(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )
