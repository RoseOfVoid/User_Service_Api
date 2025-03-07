import bcrypt

from passlib.context import CryptContext


bcrypt.__about__ = bcrypt

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__ident="2b")
