from db.models import UserBase
from .connect import engine, SessionLocal


async def get_user_db():
    async with engine.begin() as conn:
        await conn.run_sync(UserBase.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
