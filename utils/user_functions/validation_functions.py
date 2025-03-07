import re

from fastapi import HTTPException


async def check_requested_info(params:dict) -> None:
    necessary_info=['username', 'password', 'email']
    missing_info=[]
    for info in necessary_info:
        if info not in params.keys():
            missing_info.append(info)

    if missing_info:
        respond_missing_info(missing_info)

    return


def respond_missing_info(missing_params:list) -> None:
    error_message = "You didn't include yours: "
    for param in missing_params:
        error_message += f"{param}, "
    error_message = error_message.rstrip(", ")

    raise HTTPException(status_code=400, detail=error_message)


async def check_email_validity(email: str) -> None:
    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return
    raise HTTPException(status_code=400, detail="Invalid email address")


async def check_duplicity(params:dict) -> bool:
    # TODO Check Duplicity
    if True:
        return False

    raise HTTPException(status_code=400, detail="User already exists")