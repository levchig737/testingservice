from typing import Annotated

from backend.auth import User
from backend.auth.user_manager import auth_backend
from backend.auth.schemas.user import UserCreate, UserRead, UserUpdate, UserBlockByEmail
from backend.auth.user_manager import current_active_user, fastapi_users
from fastapi import APIRouter, Depends

from backend.services.user import UserService

from backend.api.deps import get_user_service

router = APIRouter()

UserDeps = Annotated[User, Depends(current_active_user)]

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)


router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])


UserServiceDeps = Annotated[UserService, Depends(get_user_service)]
user_router = APIRouter()


@user_router.get("/", response_model=list[UserRead])
async def get_all_users(
    service: UserServiceDeps
) -> list[UserRead]:

    return await service.get_all_users()


@user_router.patch("/{user_id}/", response_model=UserRead)
async def block_user_by_id(
        user_id: int, new_user: UserBlockByEmail, service: UserServiceDeps
) -> UserRead:
    return await service.update_blocked_flag(user_id, new_user)

router.include_router(user_router, prefix="/users", tags=["users"])
