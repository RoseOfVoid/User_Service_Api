from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__ident="2b")
