from fastapi import FastAPI

app = FastAPI()

fake_users = [
    {"id": 1, "name": "Vlad"},
    {"id": 2, "name": "Lera"},
    {"id": 3, "name": "Dzimka"},
]

fake_traces = [
    {"id": 1, "title": "Trace 1"},
    {"id": 2, "title": "Trace 2"},
    {"id": 3, "title": "Trace 3"},
    {"id": 4, "title": "Trace 4"},
    {"id": 5, "title": "Trace 5"},
    {"id": 6, "title": "Trace 6"},
    {"id": 7, "title": "Trace 7"},
    {"id": 8, "title": "Trace 8"},
    {"id": 9, "title": "Trace 9"},
    {"id": 10, "title": "Trace 10"},
    {"id": 11, "title": "Trace 11"},
    {"id": 12, "title": "Trace 12"},
    {"id": 13, "title": "Trace 13"},
    {"id": 14, "title": "Trace 14"},
    {"id": 15, "title": "Trace 15"},
    {"id": 16, "title": "Trace 16"},
    {"id": 17, "title": "Trace 17"},
]


@app.get("/users/{user_id}")
def get_user(user_id: int) -> list:
    return [user for user in fake_users if user["id"] == user_id]


@app.get("/traces")
def get_traces(limit: int = 100, offset: int = 0) -> list:
    return fake_traces[offset : limit + offset]
