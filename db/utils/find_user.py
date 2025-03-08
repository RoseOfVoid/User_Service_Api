from db import get_user_db
from db.models import User
from auth.settings import UserBase

from fastapi import HTTPException
from sqlalchemy.future import select


async def find_user_by_id(requested_id: str):
    async for db in get_user_db():
        result = await db.execute(select(User).filter(User.id == int(requested_id)))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
