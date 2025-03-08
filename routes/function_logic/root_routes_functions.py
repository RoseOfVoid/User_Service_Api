from db.utils import find_user_by_id, promote_user, demote_user, delete_user, change_user_status


async def promote_route_function(user_id: str):
    user_to_promote = await find_user_by_id(requested_id=user_id)
    await promote_user(user=user_to_promote)
    return {"Success", f"user {user_id} promoted"}


async def demote_route_function(user_id: str):
    user_to_promote = await find_user_by_id(requested_id=user_id)
    await demote_user(user=user_to_promote)
    return {"Success", f"user {user_id} demoted"}


async def delete_route_function(user_id: str):
    user_to_delete = await find_user_by_id(requested_id=user_id)
    await delete_user(user=user_to_delete)
    return {"Success", f"User {user_id} deleted"}


async def ban_user_function(user_id: str):
    user_to_ban = await find_user_by_id(requested_id=user_id)
    await change_user_status(user=user_to_ban, status="BANNED")
    return {"Success", f"User {user_id} banned"}


async def unban_user_function(user_id: str):
    user_to_ban = await find_user_by_id(requested_id=user_id)
    await change_user_status(user=user_to_ban, status="ACTIVE")
    return {"Success", f"User {user_id} unbanned"}
