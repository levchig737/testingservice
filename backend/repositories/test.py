from typing import Iterable, Any

from sqlalchemy.orm import joinedload

from backend.db.base_repository import BaseRepository
from backend.test.models import Test
from backend.test.schemas import TestSchemaIn
from backend.question.schemas import QuestionSchemaInScores
from sqlalchemy import delete, select, func


class TestRepository(BaseRepository):
    async def save_test(self, test: TestSchemaIn) -> Test:
        result = await self.save(Test(**test.model_dump()))
        result.max_score = 0
        result.min_score = 0
        return result

    async def get_test_by_id(self, test_id: int) -> Test:
        statement = (
            select(Test)
            .options(joinedload(Test.questions))
            .where(Test.id == test_id)
        )
        return await self.one_or_none_unique(statement)

    async def get_tests_by_theme(self, theme: str) -> Iterable[Test]:
        statement = select(Test).where(Test.theme == theme).order_by(Test.id)
        return await self.all(statement)

    async def get_all_tests(self) -> Iterable[Test]:
        statement = select(Test).order_by(Test.id)
        return await self.all(statement)

    async def get_tests_count(self) -> int:
        statement = select(func.count(Test.id))
        return await self.one(statement)

    async def update_test_by_id(self, cur_test: Test, new_test: TestSchemaIn) -> Test:

        for field, value in new_test.dict(exclude_unset=True).items():
            setattr(cur_test, field, value)

        test_res = await self.save(cur_test)
        return test_res

    async def add_scores(self, cur_test: Test, question_scores: QuestionSchemaInScores) -> Test:

        cur_test.min_score = cur_test.min_score + question_scores.min_score
        cur_test.max_score = cur_test.max_score + question_scores.max_score

        test_res = await self.save(cur_test)
        return test_res

    async def delete_test_by_id(self, test_id: int) -> None:
        query = delete(Test).where(Test.id == test_id)
        await self.session.execute(query)
        await self.session.commit()
