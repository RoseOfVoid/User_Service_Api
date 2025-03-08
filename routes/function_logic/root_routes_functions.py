from db.utils import find_user_by_id, promote_user, demote_user, delete_user, change_user_status

from fastapi import HTTPException


async def promote_route_function(user_id: str):
    user_to_promote = await find_user_by_id(requested_id=user_id)
    if not user_to_promote:
        raise HTTPException(status_code=404, detail="User not found")
    await promote_user(user=user_to_promote)
    return {"Success", f"user {user_id} promoted"}


async def demote_route_function(user_id: str):
    user_to_promote = await find_user_by_id(requested_id=user_id)
    if not user_to_promote:
        raise HTTPException(status_code=404, detail="User not found")
    await demote_user(user=user_to_promote)
    return {"Success", f"user {user_id} demoted"}


async def delete_route_function(user_id: str):
    user_to_delete = await find_user_by_id(requested_id=user_id)
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="User not found")
    await delete_user(user=user_to_delete)
    return {"Success", f"User {user_id} deleted"}


async def ban_user_function(user_id: str):
    user_to_ban = await find_user_by_id(requested_id=user_id)
    if not user_to_ban:
        raise HTTPException(status_code=404, detail="User not found")
    await change_user_status(user=user_to_ban, status="BANNED")
    return {"Success", f"User {user_id} banned"}


async def unban_user_function(user_id: str):
    user_to_ban = await find_user_by_id(requested_id=user_id)
    if not user_to_ban:
        raise HTTPException(status_code=404, detail="User not found")
    await change_user_status(user=user_to_ban, status="ACTIVE")
    return {"Success", f"User {user_id} unbanned"}