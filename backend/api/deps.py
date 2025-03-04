from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_async_session
from services.answer import AnswerService
from services.completed_tests_users import CompletedTestsUsersService
from services.question import QuestionService
from services.right_answer import RightAnswerService
from services.test import TestService
from services.user import UserService


async def get_test_service(session: AsyncSession = Depends(get_async_session)) -> TestService:
    return TestService(session=session)


async def get_question_service(session: AsyncSession = Depends(get_async_session)) -> QuestionService:
    return QuestionService(session=session)


async def get_answer_service(session: AsyncSession = Depends(get_async_session)) -> AnswerService:
    return AnswerService(session=session)


async def get_right_answer_service(session: AsyncSession = Depends(get_async_session)) -> RightAnswerService:
    return RightAnswerService(session=session)


async def get_user_service(session: AsyncSession = Depends(get_async_session)) -> UserService:
    return UserService(session=session)


async def get_completed_tests_users_service(session: AsyncSession = Depends(get_async_session)) \
        -> CompletedTestsUsersService:
    return CompletedTestsUsersService(session=session)

