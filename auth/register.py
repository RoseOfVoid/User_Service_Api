from db.utils import create_new_user

from fastapi import HTTPException
from fastapi.responses import JSONResponse


async def register_user(data: dict):
    try:
        await create_new_user(data=data)
        return JSONResponse(status_code=201, content={"Success": f"User {data['username']} "
                                                                 f"was successfully registered"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
