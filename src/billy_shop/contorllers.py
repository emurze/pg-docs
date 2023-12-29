from src.app import app
from src.billy_shop.domain import User


@app.get("/")
def hello(user: User, title: str = "Lerka") -> dict:
    return {
        "user": user["name"],
        "title": title,
    }
