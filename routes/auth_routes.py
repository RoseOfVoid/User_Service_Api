from .function_logic.auth_routes_functions import register_user_function, login_user_function
from auth.settings import Token
from auth.utils import get_user_from_token
from auth.wrappers import admin_required

from fastapi import APIRouter, Request, Depends

router = APIRouter()


@router.post("/register")
async def register_user_route(request: Request):
    return await register_user_function(request)


@router.post("/login", response_model=Token)
async def login_user_route(request: Request):
    return await login_user_function(request)


@router.get("/protected-endpoint")
def protected_route(user: dict = Depends(get_user_from_token)):
    return {"message": "Access granted", "user": user}


@router.get("/hello")
@admin_required
async def hello_route(user: dict = Depends(get_user_from_token)):
    return {"message": "Hello World"}
