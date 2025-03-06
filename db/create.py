import os

import asyncpg
from dotenv import load_dotenv

load_dotenv()

DSN = (f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:"
       f"{os.getenv('DB_PORT')}/postgres")

async def check_if_db_exists() -> bool:
    try:
        conn = await asyncpg.connect(dsn=DSN)
        result = await conn.fetch(f"SELECT 1 FROM pg_database WHERE datname = '{os.getenv("DB_DEFAULT")}'")
        await conn.close()
        return bool(result)
    except Exception as e:
        print(f"Error while connecting to database: {e}")
        return False


async def create_database() -> None:
    try:
        conn = await asyncpg.connect(dsn=DSN)
        await conn.execute(f"CREATE DATABASE IF NOT EXISTS '{os.getenv("DB_DEFAULT")}'")
        print("Database created successfully")
        await conn.close()
    except Exception as e:
        print(f"Error while creating database: {e}")


async def check_db_connection() -> None:
    exist = await check_if_db_exists()
    if not exist:
        await create_database()
    else:
        print("Successfully connected to database")

