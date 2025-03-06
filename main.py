from db import check_db_connection
from routes.auth_routes import router as auth_router

import asyncio

from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(auth_router)


async def main():
    await check_db_connection()
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)


if __name__ == '__main__':
    asyncio.run(main())
