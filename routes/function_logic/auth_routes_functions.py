from utils import (check_requested_info, check_email_validity, check_login_info)
from auth import register_user, login_user
from auth.utils import PasswordManager
from db.utils import check_duplicity

from fastapi import Request


async def register_user_function(request: Request):
    params = dict(request.headers)
    await check_requested_info(params)
    await check_email_validity(params['email'])
    pw = PasswordManager(password=params['password'], length_req=True, numbers_req=True, special_chars_req=True)
    await pw.validate_password()
    params['password'] = pw.hash_password()
    await check_duplicity(username=params['username'], email=params['email'])

    return await register_user(data=params)


async def login_user_function(request: Request):
    params = dict(request.headers)
    await check_login_info(params)
    return await login_user(data=params)
