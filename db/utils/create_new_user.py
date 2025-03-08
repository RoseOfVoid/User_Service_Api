from db.models import User
from db import get_user_db


async def create_new_user(data: dict, role: str = "USER"):
    async for db in get_user_db():
        new_user = User(username=data['username'],
                        email=data['email'],
                        password=data['password'],
                        role=role,
                        status="ACTIVE")
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
