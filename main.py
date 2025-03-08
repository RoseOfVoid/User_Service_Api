from db import check_db_connection
from routes.auth_routes import router as auth_router
from routes.root_routes import router as root_router
from routes.admin_routes import router as admin_router
from utils import execute_params

import asyncio
import sys

from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(root_router)


async def main():
    await check_db_connection()
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        execute_params(param=sys.argv[1])
    else:
        asyncio.run(main())

