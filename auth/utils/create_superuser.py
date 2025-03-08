from auth.utils import hash_password
from db.utils import create_new_user, find_root_users

import getpass

SINGLE_ROOT = True


async def create_superuser():
    if SINGLE_ROOT:
        users = await find_root_users()
        if users:
            raise ValueError("Root user already exist")

    username = input("Enter your username (default is root): ")
    username = username or "root"

    password = getpass.getpass("Enter your password: ")
    if not password:
        raise ValueError("You must enter your password")

    conf_password = getpass.getpass("Confirm your password: ")
    if conf_password != password:
        raise ValueError("Passwords don't match")

    email = input("Enter your email address (default is root@example.com): ")
    email = email or "root@example.com"

    hashed_password = hash_password(password)

    await create_new_user(data={"username": username,
                                "email": email,
                                "password": hashed_password,
                                },
                          role="ROOT")
