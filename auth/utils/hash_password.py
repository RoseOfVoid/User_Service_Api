from werkzeug.security import generate_password_hash


def hash_password(password):
    return generate_password_hash(password=password, salt_length=8)
