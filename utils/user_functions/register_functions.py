from db.models import User
from db import get_user_db
from db.connect import engine

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Response


async def register_user_to_db(data: dict):
    try:
        async for db in get_user_db():
            new_user = User(username=data['username'],
                            email=data['email'],
                            password=data['password'],
                            role="USER",
                            status="ACTIVE")
            db.add(new_user)
            await db.commit()
            await db.refresh(new_user)
            return {"Success": f"New user {data['username']} created"}
    except Exception as e:
        return {"Error": str(e)}
