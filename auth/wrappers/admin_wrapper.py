from functools import wraps

from fastapi import HTTPException


def admin_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if int(user.role) <= 1:
            return await func(*args, **kwargs)
        raise HTTPException(status_code=403, detail="Admin access required")
    return wrapper
