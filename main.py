from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from controllers.TodoControllers import todo_router
from controllers.UserController import user_router
from controllers.UserTodoControler import user_todo_router
from database import init_db
from errors.ErrorHandlers import register_error_handlers

app = FastAPI()


class Todo(BaseModel):
    id: Optional[int]
    label: str


todos = []


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/test")
async def test():
    return {"message": "Dobry den. Nashledanou."}


app.include_router(todo_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")
app.include_router(user_todo_router, prefix="/api/v1")

register_error_handlers(app)
