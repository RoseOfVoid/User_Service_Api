from db.models import User
from auth.settings import UserBase


def convert_user_from_db(user: User) -> UserBase:
    return UserBase(id=int(user.id),
                    username=str(user.username),
                    email=str(user.email),
                    role=str(user.get_role()),
                    status=str(user.get_status()))
