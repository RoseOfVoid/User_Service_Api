from db.utils import delete_user, find_user_by_id


from fastapi import HTTPException


async def get_profile_function(user: dict):
    return user


async def delete_profile_function(request, user: dict):
    password = request.headers.get('password')
    if not password:
        raise HTTPException(status_code=401, detail="Please Provide your password to confirm account delete")
    user_db = await find_user_by_id(user.id)
    await delete_user(user_db)
    return {"Success": "Profile Deleted"}
