from auth.wrappers import admin_required
from auth.utils import get_user_from_token
from .function_logic.admin_routes_functions import *

from fastapi import APIRouter, Depends

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/users")
@admin_required
async def get_all_users(user: dict = Depends(get_user_from_token)):
    return await get_all_users_function()


@router.get("/users/{user_id}")
@admin_required
async def get_user_by_id(user_id: str, user: dict = Depends(get_user_from_token)):
    return await get_user_by_id_function(user_id=user_id)


@router.post("/ban/{user_id}")
@admin_required
async def ban_user(user_id: str, user: dict = Depends(get_user_from_token)):
    return await admin_ban_user_function(user_id=user_id)


@router.post("/unban/{user_id}")
@admin_required
async def unban_user(user_id: str, user: dict = Depends(get_user_from_token)):
    return await admin_unban_user_function(user_id=user_id)
