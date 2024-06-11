from fastapi_users import schemas
from pydantic import BaseModel

from auth.models.user import UserRole


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    role: UserRole
    blocked_flag: bool


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    role: UserRole = UserRole.user
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    blocked_flag: bool = False


class UserUpdate(schemas.BaseUserUpdate):
    email: str
    password: str
    role: UserRole


class UserBlockByEmail(BaseModel):
    blocked_flag: bool
