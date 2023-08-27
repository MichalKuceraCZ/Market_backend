from database import async_session
from services.TodoService import TodoService
from services.UserService import UserService
from services.UserTodoService import UserTodoService
from services.AssetService import AssetService


async def get_todo_service():
    async with async_session() as session:
        async with session.begin():
            yield TodoService(session)


async def get_user_service():
    async with async_session() as session:
        async with session.begin():
            yield UserService(session)


async def get_user_todo_service():
    async with async_session() as session:
        async with session.begin():
            yield UserTodoService(session)


async def get_asset_service():
    async with async_session() as session:
        async with session.begin():
            yield AssetService(session)
