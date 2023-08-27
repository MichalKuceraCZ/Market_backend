from database import async_session, api_key
from services.AssetService import AssetService
from services.TodoService import TodoService
from services.UserService import UserService
from services.UserTodoService import UserTodoService
from services.PolygonService import PolygonService


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


global_context = {
    "api_key": api_key,
}


async def get_polygon_service():
    async with async_session() as session:
        async with session.begin():
            context = {**global_context, "session": session}

            yield PolygonService(context)
