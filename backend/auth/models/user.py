from db.base import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import  String
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum as BaseEnum


# Перечисление для типа роли
class UserRole(str, BaseEnum):
    admin = "admin"  # Все права
    user = "user"  # Прохождение тестов


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)  # type: ignore
    blocked_flag: Mapped[bool] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(nullable=False)

    email: Mapped[str] = mapped_column(unique=True)  # type: ignore
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=True, nullable=False)
