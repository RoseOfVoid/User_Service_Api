from auth.settings import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM

import os
from datetime import datetime, timedelta, UTC
from typing import Optional

from jose import jwt


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(UTC) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=ALGORITHM)
