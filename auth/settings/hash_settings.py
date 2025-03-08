import bcrypt

from passlib.context import CryptContext


bcrypt.__about__ = bcrypt

bcrypt_context = CryptContext(schemes=["bcrypt", "ldap_salted_md5"],
                              ldap_salted_md5__salt_size=16,
                              deprecated="auto")
