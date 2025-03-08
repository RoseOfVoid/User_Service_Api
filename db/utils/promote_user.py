from db import get_user_db
from db.models import User

from fastapi import HTTPException
from sqlalchemy import text


async def promote_user(user: User):
    async for db in get_user_db():
        if user.get_role() == 0:
            raise HTTPException(status_code=400, detail="Cannot promote root user")
        query_string = f"UPDATE users SET role='ADMIN' WHERE id={user.id}"
        await db.execute(text(query_string))
        await db.commit()
        await db.flush()
