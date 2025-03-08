from functools import wraps

from fastapi import HTTPException


def root_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if int(user.role) == 0:
            return await func(*args, **kwargs)
        raise HTTPException(status_code=403, detail="Root access required")
    return wrapper
