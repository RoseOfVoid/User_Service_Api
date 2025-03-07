from werkzeug.security import check_password_hash
from fastapi import HTTPException


async def check_password(password: str, hashed_password: str) -> None:
    if not check_password_hash(password=password, pwhash=hashed_password):
        raise HTTPException(status_code=403, detail="Incorrect password")
