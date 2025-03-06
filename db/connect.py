from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("DB_PASSWORD")
username = os.getenv("DB_USER")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_DEFAULT")

CONNECTION_STRING = f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}"
db = create_async_engine(CONNECTION_STRING, echo=True)

AsyncSessionLocal = sessionmaker(bind=db, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """Function to get an async database session"""
    async with AsyncSessionLocal() as session:
        yield session
