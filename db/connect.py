import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv


load_dotenv()

password = os.getenv("DB_PASSWORD")
username = os.getenv("DB_USER")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_DEFAULT")

CONNECTION_STRING = f"postgresql+asyncpg://{username}:{password}@{host}:{port}"
CONNECTION_STRING_DB = f"{CONNECTION_STRING}/{database}"

engine = create_async_engine(CONNECTION_STRING_DB)


SessionLocal = async_sessionmaker(engine)
