from db import get_user_db
from db.models import User

from sqlalchemy import text


async def change_user_status(user: User, status: str):
    async for db in get_user_db():
        query_string = f"UPDATE users SET status='{status}' WHERE id={user.id}"
        await db.execute(text(query_string))
        await db.commit()
        await db.flush()
