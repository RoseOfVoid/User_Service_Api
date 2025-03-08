import enum
from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Status(enum.Enum):
    ACTIVE = "ACTIVE"
    UNAUTHORIZED = "UNAUTHORIZED"
    BANNED = "BANNED"


class Role(enum.Enum):
    ROOT = 0
    ADMIN = 1
    USER = 2


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(500), nullable=False)
    email = Column(String(50), nullable=False)
    role = Column(Enum(Role), name="role")
    status = Column(Enum(Status), name="status")
    created = Column(DateTime, nullable=False, default=func.now())

    def get_role(self) -> str:
        return self.role.value

    def get_status(self) -> str:
        return str(self.status.value)
