from db.models import User
from db import get_user_db

from fastapi import HTTPException
from fastapi.responses import JSONResponse


async def register_user(data: dict):
    try:
        async for db in get_user_db():
            new_user = User(username=data['username'],
                            email=data['email'],
                            password=data['password'],
                            role="USER",
                            status="ACTIVE")
            db.add(new_user)
            await db.commit()
            await db.refresh(new_user)
            return JSONResponse(status_code=201, content={"Success": f"User {data['username']} "
                                                                     f"was successfully registered"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
