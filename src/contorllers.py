from src.app import app
from src.domain import User


@app.get('/')
def view(user: User, title: str = 'Lerka') -> dict:
    return {
        'user': user['name'],
        'title': title,
    }
