from sqlalchemy_utils import database_exists, create_database

from connect import db
from models import UserBase


def create_db():
    if not database_exists(db.url):
        create_database(db.url)

    UserBase.metadata.create_all(db)