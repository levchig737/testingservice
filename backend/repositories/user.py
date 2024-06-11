from typing import Iterable

from db.base_repository import BaseRepository
from auth.models.user import User
from auth.schemas.user import UserBlockByEmail, UserRole
from sqlalchemy import select


class UserRepository(BaseRepository):
    async def get_user_by_id(self, test_id: int) -> User | None:
        statement = (
            select(User)
            .where(User.id == test_id)
        )
        return await self.one_or_none(statement)

    async def get_all_users(self) -> Iterable[User]:
        statement = select(User).order_by(User.id)
        return await self.all(statement)

    async def update_blocked_flag(self, cur_test: User, new_test: UserBlockByEmail) -> User:

        cur_test.blocked_flag = new_test.blocked_flag

        test_res = await self.save(cur_test)
        return test_res
