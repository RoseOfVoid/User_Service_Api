from auth.utils import get_user_from_token
from auth.wrappers import root_required
from .function_logic.root_routes_functions import promote_route_function, demote_route_function, delete_route_function

from fastapi import APIRouter, Depends

router = APIRouter(prefix="/root", tags=["root"])


@router.post("/promote/{user_id}")
@root_required
async def promote_route(user_id: str, user: dict = Depends(get_user_from_token)):
    return await promote_route_function(user_id=user_id, user=user)


@router.post("/demote/{user_id}")
@root_required
async def demote_route(user_id: str, user: dict = Depends(get_user_from_token)):
    return await demote_route_function(user_id=user_id, user=user)


@router.delete("/delete/{user_id}")
@root_required
async def delete_route(user_id: str, user: dict = Depends(get_user_from_token)):
    return await delete_route_function(user_id=user_id, user=user)