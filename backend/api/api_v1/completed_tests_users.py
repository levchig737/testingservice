from typing import Annotated, List

from fastapi import APIRouter, Depends

from auth import User
from auth.user_manager import current_active_user
from completed_tests_users.schemas import (
    CompletedTestsUsersSchemaIn, CompletedTestsUsersSchemaOut,
    CompletedTestsUsersScoresSchemaOut
)
from services.completed_tests_users import CompletedTestsUsersService

from api.deps import get_completed_tests_users_service


router = APIRouter()

CompletedTestsUsersServiceDeps = Annotated[CompletedTestsUsersService, Depends(get_completed_tests_users_service)]
UserDeps = Annotated[User, Depends(current_active_user)]


@router.post("/", response_model=CompletedTestsUsersSchemaOut)
async def create_completed_test(
    new_test: CompletedTestsUsersSchemaIn, user: UserDeps, service: CompletedTestsUsersServiceDeps
) -> CompletedTestsUsersSchemaOut:
    return await service.save_completed_tests_users(new_test, user.blocked_flag)


@router.get("/{test_id}/", response_model=CompletedTestsUsersSchemaOut)
async def get_completed_test_by_id(
    test_id: int, user: UserDeps, service: CompletedTestsUsersServiceDeps
) -> CompletedTestsUsersSchemaOut:
    return await service.get_completed_tests_by_id(test_id, user.blocked_flag)


@router.get("/last_completed_test/", response_model=CompletedTestsUsersSchemaOut)
async def get_last_completed_test(
    test_id: int, user_id: int, service: CompletedTestsUsersServiceDeps
) -> CompletedTestsUsersSchemaOut:
    return await service.get_last_completed_tests_users(test_id, user_id)


@router.get("/last_test_scores/", response_model=CompletedTestsUsersScoresSchemaOut)
async def get_last_completed_tests_users_scores(
    test_id: int, user_id: int, service: CompletedTestsUsersServiceDeps
) -> CompletedTestsUsersScoresSchemaOut:
    return await service.get_last_completed_tests_users_scores(test_id, user_id)


@router.get("/", response_model=List[CompletedTestsUsersSchemaOut])
async def get_all_completed_tests(
        user: UserDeps, service: CompletedTestsUsersServiceDeps
) -> List[CompletedTestsUsersSchemaOut]:
    return await service.get_all_completed_tests_users_scores(user.blocked_flag)


@router.patch("/{test_id}/", response_model=CompletedTestsUsersSchemaOut)
async def update_completed_test_scores(
    test_id: int, new_test: CompletedTestsUsersSchemaIn, service: CompletedTestsUsersServiceDeps
) -> CompletedTestsUsersSchemaOut:
    return await service.update_completed_tests_users_scores(test_id, new_test)


@router.delete("/{test_id}/", response_model=None)
async def delete(test_id: int, service: CompletedTestsUsersServiceDeps) -> None:
    return await service.delete_test_by_id(test_id)
