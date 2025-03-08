from db import get_user_db
from db.models import User

from sqlalchemy.future import select


async def find_user_by_id(requested_id: str):
    async for db in get_user_db():
        result = await db.execute(select(User).filter(User.id == int(requested_id)))
        user = result.scalars().first()
        return user


async def find_all_users():
    async for db in get_user_db():
        result = await db.execute(select(User))
        users = result.scalars().all()
        return users
