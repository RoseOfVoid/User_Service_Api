from auth.settings import oauth2_bearer, ALGORITHM
from db.utils import find_user_by_id
from auth.utils.prepare_user_from_db import convert_user_from_db

import os

from fastapi import Depends, HTTPException
from jose import JWTError, jwt


async def get_user_from_token(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user_db = await find_user_by_id(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    return convert_user_from_db(user_db)
