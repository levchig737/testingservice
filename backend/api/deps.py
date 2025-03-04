from db.base import get_session_stub, get_async_session
from fastapi import Depends

from main import app
from services.test import TestService
from services.question import QuestionService
from services.answer import AnswerService
from services.right_answer import RightAnswerService
from services.user import UserService
from services.completed_tests_users import CompletedTestsUsersService

from sqlalchemy.ext.asyncio import AsyncSession


async def get_test_service(session: AsyncSession = Depends(get_session_stub)) -> TestService:
    return TestService(session=session)


async def get_question_service(session: AsyncSession = Depends(get_session_stub)) -> QuestionService:
    return QuestionService(session=session)


async def get_answer_service(session: AsyncSession = Depends(get_session_stub)) -> AnswerService:
    return AnswerService(session=session)


async def get_right_answer_service(session: AsyncSession = Depends(get_session_stub)) -> RightAnswerService:
    return RightAnswerService(session=session)


async def get_user_service(session: AsyncSession = Depends(get_session_stub)) -> UserService:
    return UserService(session=session)


async def get_completed_tests_users_service(session: AsyncSession = Depends(get_session_stub)) \
        -> CompletedTestsUsersService:
    return CompletedTestsUsersService(session=session)


# --- Dependency Injection (DI) через `app.dependency_overrides` --- #

app.dependency_overrides[get_session_stub] = get_async_session