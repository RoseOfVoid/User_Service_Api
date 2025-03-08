from db import get_user_db
from db.models import User

from fastapi import HTTPException
from sqlalchemy import text


async def delete_user(user: User):
    async for db in get_user_db():
        await db.delete(user)
        await db.commit()
        await db.flush()
