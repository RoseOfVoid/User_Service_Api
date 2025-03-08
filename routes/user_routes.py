from auth.utils import get_user_from_token
from .function_logic.user_routes_functions import *

from fastapi import APIRouter, Depends, Request

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/profile")
async def get_profile_route(user: dict = Depends(get_user_from_token)):
    return await get_profile_function(user)


@router.delete("/delete")
async def delete_profile_route(request: Request, user: dict = Depends(get_user_from_token)):
    return await delete_profile_function(request, user)
