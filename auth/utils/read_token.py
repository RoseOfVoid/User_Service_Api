from auth.settings import oauth2_bearer, ALGORITHM
from db.utils import find_user_by_id

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

    return await find_user_by_id(user_id)
