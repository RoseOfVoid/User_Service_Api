from db.utils import find_all_users, find_user_by_id, change_user_status
from auth.settings import UserBase


from fastapi import HTTPException


async def get_all_users_function():
    users_from_db = await find_all_users()
    users = []
    for user in users_from_db:
        users.append(UserBase(id=int(user.id),
                              username=user.username,
                              email=user.email,
                              role=user.role.name,
                              status=user.status))

    return users


async def get_user_by_id_function(user_id: str):
    user = await find_user_by_id(user_id)
    return UserBase(id=int(user.id),
                              username=user.username,
                              email=user.email,
                              role=user.role.name,
                              status=user.status)



async def admin_ban_user_function(user_id: str):
    user_to_ban = await find_user_by_id(user_id)
    if int(user_to_ban.get_role()) <= 1:
        raise HTTPException(status_code=403, detail="Cannot ban admin or root")
    await change_user_status(user_to_ban, "BANNED")
    return {"Success": f"User {user_id} has been banned"}


async def admin_unban_user_function(user_id: str):
    user_to_ban = await find_user_by_id(user_id)
    if int(user_to_ban.get_role()) <= 1:
        raise HTTPException(status_code=403, detail="Cannot unban admin or root")
    await change_user_status(user_to_ban, "ACTIVE")
    return {"Success": f"User {user_id} has been unbanned"}
