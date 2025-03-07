from db.models import User
from db import get_user_db
from .utils import check_password

from fastapi import HTTPException
from sqlalchemy.future import select


async def login_user(data: dict):
    async for db in get_user_db():
        result = await db.execute(select(User).filter(User.username == data['username']))
        user_to_login = result.scalars().first()
        if not user_to_login:
            raise HTTPException(status_code=404, detail="User not found")
        await check_password(data['password'], user_to_login.password)
    return {"Success": "Logged in"}
