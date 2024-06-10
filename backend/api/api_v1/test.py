from typing import Annotated

from fastapi import APIRouter, Depends

from backend.auth import User
from backend.auth.user_manager import current_active_user
from backend.test.schemas import TestSchemaIn, TestSchemaOut, TestSchemaWithoutQuestions, TestSchemaCount, \
    TestSchemaAverageResult
from backend.services.test import TestService

from backend.api.deps import get_test_service


router = APIRouter()

TestServiceDeps = Annotated[TestService, Depends(get_test_service)]
UserDeps = Annotated[User, Depends(current_active_user)]


@router.post("/")
async def create_test(
    new_test: TestSchemaIn, service: TestServiceDeps
) -> TestSchemaWithoutQuestions:
    return await service.save_test(new_test)


@router.get("/", response_model=list[TestSchemaWithoutQuestions])
async def get_all_tests(
    service: TestServiceDeps, user: UserDeps
) -> list[TestSchemaWithoutQuestions]:

    return await service.get_all_tests(user.blocked_flag)


@router.get("/count/", response_model=TestSchemaCount)
async def get_tests_count(
    service: TestServiceDeps
) -> TestSchemaCount:

    return await service.get_tests_count()


@router.get("/without_questions/{test_id}/", response_model=TestSchemaIn)
async def get_test_by_id(
    test_id: int, service: TestServiceDeps
) -> TestSchemaWithoutQuestions:

    return await service.get_test_by_id(test_id)


@router.get("/with_questions/{test_id}/", response_model=TestSchemaOut)
async def get_test_by_id_with_questions(
    test_id: int, user: UserDeps, service: TestServiceDeps
) -> TestSchemaOut:

    return await service.get_test_by_id_with_questions(test_id, user.blocked_flag)


@router.get("/themes/{theme}/", response_model=list[TestSchemaIn])
async def get_test_by_theme(
        theme: str, service: TestServiceDeps
) -> list[TestSchemaWithoutQuestions]:

    return await service.get_test_by_theme(theme)


@router.get("/average_result/{test_id}/", response_model=TestSchemaAverageResult)
async def get_average_result_users(
        test_id: int, service: TestServiceDeps
) -> TestSchemaAverageResult:

    return await service.get_average_result_users(test_id)


@router.patch("/{test_id}/", response_model=TestSchemaIn)
async def update_test(
        test_id: int, new_test: TestSchemaIn, service: TestServiceDeps
) -> TestSchemaWithoutQuestions:
    return await service.update_test(test_id, new_test)


@router.delete("/{test_id}/", response_model=None)
async def delete(test_id: int, service: TestServiceDeps) -> None:

    return await service.delete_test_by_id(test_id)
