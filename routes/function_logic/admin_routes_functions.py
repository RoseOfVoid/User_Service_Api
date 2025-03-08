from db.utils import find_all_users
from auth.settings import UserBase


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
