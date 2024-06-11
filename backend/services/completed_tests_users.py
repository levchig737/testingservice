from fastapi import HTTPException

from completed_tests_users.schemas import (CompletedTestsUsersSchemaIn, CompletedTestsUsersSchemaOut,
                                                   CompletedTestsUsersScoresSchemaOut)
from repositories.completed_tests_users import CompletedTestsUsersRepository

from sqlalchemy.ext.asyncio import AsyncSession


def validate_blocked_user(blocked_flag: bool) -> bool:
    return blocked_flag


class CompletedTestsUsersService:
    def __init__(self, session: AsyncSession):
        self.repository = CompletedTestsUsersRepository(session)

    async def save_completed_tests_users(self, test_schema: CompletedTestsUsersSchemaIn, blocked_flag: bool
                                         ) -> CompletedTestsUsersSchemaOut:

        if validate_blocked_user(blocked_flag):
            raise HTTPException(status_code=400, detail="USER_BLOCKED")

        test = await self.repository.save_completed_tests_users(test_schema)

        return CompletedTestsUsersSchemaOut(
            id=test.id, test_id=test.test_id, user_id=test.user_id, scores=test.scores
        )

    async def get_completed_tests_by_id(
            self, test_id: int, blocked_flag: bool
    ) -> CompletedTestsUsersSchemaOut:
        test = await self.repository.get_completed_tests_users_by_id(test_id)
        if validate_blocked_user(blocked_flag):
            raise HTTPException(status_code=400, detail="USER_BLOCKED")

        return CompletedTestsUsersSchemaOut(
            test_id=test.test_id, user_id=test.user_id, scores=test.scores
        )

    async def get_last_completed_tests_users(
            self, test_id: int, user_id: int
    ) -> CompletedTestsUsersSchemaOut:
        test = await self.repository.get_last_completed_tests_users(test_id, user_id)

        return CompletedTestsUsersSchemaOut(
            test_id=test.test_id, user_id=test.user_id, scores=test.scores
        )

    async def get_last_completed_tests_users_scores(
            self, test_id: int, user_id: int
    ) -> CompletedTestsUsersScoresSchemaOut:
        test = await self.repository.get_last_completed_tests_users(test_id, user_id)

        return CompletedTestsUsersScoresSchemaOut(
            scores=test.scores
        )

    async def get_all_completed_tests_users_scores(
            self, blocked_flag: bool
    ) -> list[CompletedTestsUsersSchemaOut]:

        if validate_blocked_user(blocked_flag):
            raise HTTPException(status_code=400, detail="USER_BLOCKED")

        tests = await self.repository.get_all_completed_tests_users()
        tests_out = []

        for test in tests:
            tests_out.append(CompletedTestsUsersSchemaOut(
                test_id=test.test_id, user_id=test.user_id, scores=test.scores
            ))

        return tests_out

    async def update_completed_tests_users_scores(
            self, test_id: int, new_test: CompletedTestsUsersSchemaIn,
    ) -> CompletedTestsUsersSchemaOut:
        cur_test = await self.repository.get_completed_tests_users_by_id(test_id)

        test = await self.repository.update_completed_tests_users_by_id(cur_test=cur_test, new_test=new_test)

        return CompletedTestsUsersSchemaOut(
            test_id=test.test_id, user_id=test.user_id, scores=test.scores
        )

    async def delete_test_by_id(self, test_id: int) -> None:
        await self.repository.delete_completed_tests_users_by_id(test_id=test_id)
