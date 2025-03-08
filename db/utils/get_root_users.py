from db import get_user_db
from db.models import User

from sqlalchemy.future import select


async def find_root_users():
    async for db in get_user_db():
        result = await db.execute(select(User).filter(User.role == "ROOT"))
        users = result.scalars().all()
        return users
