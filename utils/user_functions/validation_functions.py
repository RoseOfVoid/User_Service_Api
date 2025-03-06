import re

from fastapi import HTTPException


def check_requested_info(params:dict) -> list | None:
    necessary_info=['username', 'password', 'email']
    missing_info=[]
    for info in necessary_info:
        if info not in params.keys():
            missing_info.append(info)

    return missing_info


def respond_missing_info(missing_params:list) -> HTTPException:
    error_message = "You must include your: "
    for param in missing_params:
        error_message += f"{param}, "

    return HTTPException(status_code=400, detail=error_message) #TODO: Repair respoce


def check_email_validity(email:str) -> bool:
    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return True
    return False


def check_duplicity(params:dict) -> bool:
    #TODO: Connect to DB and check for duplicity
    return False