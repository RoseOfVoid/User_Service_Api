from auth.token import bcrypt_context
from fastapi import HTTPException


def hash_password(password: str) -> str:
    hash_pw = bcrypt_context.hash(password)
    print(hash_pw)
    return hash_pw


async def check_password(password: str, hashed_password: str) -> None:
    if not bcrypt_context.verify(password, hashed_password):
        raise HTTPException(status_code=403, detail="Incorrect password")
