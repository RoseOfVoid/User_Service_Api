from auth.wrappers import admin_required
from auth.utils import get_user_from_token
from .function_logic.admin_routes_functions import get_all_users_function

from fastapi import APIRouter, Depends

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/users")
@admin_required
async def get_all_users(user: dict = Depends(get_user_from_token)):
    return await get_all_users_function()
