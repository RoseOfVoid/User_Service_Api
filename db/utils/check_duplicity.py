from db import get_user_db
from db.models import User

from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


async def check_duplicity(username: str, email: str) -> None:
    async for db in get_user_db():
        await check_username_duplicity(username, db)
        await check_email_duplicity(email, db)


async def check_username_duplicity(username: str, db: AsyncSession) -> None:
    result = await db.execute(select(User).filter(User.username == username))
    dup_username = result.fetchone()
    if dup_username:
        raise HTTPException(status_code=400, detail="Username already exists")


async def check_email_duplicity(email: str, db: AsyncSession) -> None:
    result = await db.execute(select(User).filter(User.email == email))
    dup_email = result.fetchone()
    if dup_email:
        raise HTTPException(status_code=400, detail="Email already exists")
