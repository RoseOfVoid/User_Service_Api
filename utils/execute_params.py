from auth.utils import create_superuser
from db import check_db_connection

import asyncio


async def superuser_creation():
    await check_db_connection()
    await create_superuser()


def execute_params(param: str):
    match param:
        case "createsuperuser":
            asyncio.run(superuser_creation())
        case _:
            raise ValueError(f"Unknown command")
