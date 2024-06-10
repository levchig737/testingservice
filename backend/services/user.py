from backend.auth.schemas.user import UserBlockByEmail, UserRead
from backend.repositories.user import UserRepository

from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    async def get_all_users(
            self
    ) -> list[UserRead]:

        tests = await self.repository.get_all_users()
        tests_out = []

        for test in tests:
            tests_out.append(UserRead(
                id=test.id, email=test.email, role=test.role, blocked_flag=test.blocked_flag
            ))

        return tests_out

    async def update_blocked_flag(
            self, test_id: int, new_test: UserBlockByEmail,
    ) -> UserRead:
        cur_test = await self.repository.get_user_by_id(test_id)

        test = await self.repository.update_blocked_flag(cur_test=cur_test, new_test=new_test)

        return UserRead(
            id=test.id, email=test.email, role=test.role, blocked_flag=test.blocked_flag
        )
