from typing import Iterable

from backend.db.base_repository import BaseRepository
from backend.completed_tests_users.models import CompletedTestsUsers
from backend.completed_tests_users.schemas import CompletedTestsUsersSchemaIn
from sqlalchemy import delete, select


class CompletedTestsUsersRepository(BaseRepository):
    async def save_completed_tests_users(self, test: CompletedTestsUsersSchemaIn) -> CompletedTestsUsers:
        result = await self.save(CompletedTestsUsers(**test.model_dump()))
        return result

    async def get_completed_tests_users_by_id(self, test_id: int) -> CompletedTestsUsers | None:
        statement = (
            select(CompletedTestsUsers)
            .where(CompletedTestsUsers.id == test_id)
        )
        return await self.one_or_none(statement)

    async def get_last_completed_tests_users(self, test_id: int, user_id: int) -> CompletedTestsUsers | None:
        statement = (
            select(CompletedTestsUsers)
            .where(
                CompletedTestsUsers.test_id == test_id,
                CompletedTestsUsers.user_id == user_id
            )
            .order_by(CompletedTestsUsers.id.desc())
            .limit(1)
        )

        return await self.one_or_none(statement)

    async def get_all_completed_tests_users(self) -> Iterable[CompletedTestsUsers]:
        statement = select(CompletedTestsUsers).order_by(CompletedTestsUsers.id)
        return await self.all(statement)

    async def get_all_completed_tests_users_by_test_id(self, test_id: int) -> Iterable[CompletedTestsUsers]:
        statement = (select(CompletedTestsUsers)
                     .where(CompletedTestsUsers.test_id == test_id)
                     .order_by(CompletedTestsUsers.id))
        return await self.all(statement)

    async def update_completed_tests_users_by_id(self, cur_test: CompletedTestsUsers, new_test: CompletedTestsUsersSchemaIn) \
            -> CompletedTestsUsers:

        for field, value in new_test.dict(exclude_unset=True).items():
            setattr(cur_test, field, value)

        test_res = await self.save(cur_test)
        return test_res

    async def delete_completed_tests_users_by_id(self, test_id: int) -> None:
        query = delete(CompletedTestsUsers).where(CompletedTestsUsers.id == test_id)
        await self.session.execute(query)
        await self.session.commit()
