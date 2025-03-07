from utils import check_requested_info, check_duplicity, check_email_validity
from auth import register_user

from fastapi import Request


async def register_user_function(request: Request):
    params = dict(request.query_params)
    await check_requested_info(params)
    await check_email_validity(params['email'])
    await check_duplicity(params)

    return await register_user(data=params)
