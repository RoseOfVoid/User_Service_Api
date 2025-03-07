from .function_logic.auth_routes_functions import register_user_function

from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/register")
async def register_user_route(request: Request):
    return await register_user_function(request)
