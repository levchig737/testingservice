from typing import Iterable

from backend.db.base_repository import BaseRepository
from backend.right_answer.models.right_answer import RightAnswer
from backend.right_answer.schemas import RightAnswerSchema, RightAnswerSchemaIn
from sqlalchemy import delete, select


class RightAnswerRepository(BaseRepository):
    async def save_answer(self, test: RightAnswerSchemaIn) -> RightAnswer:
        result = await self.save(RightAnswer(**test.model_dump()))
        return result

    async def get_answer_by_id(self, question_id: int) -> RightAnswer | None:
        statement = select(RightAnswer).where(RightAnswer.id == question_id)
        return await self.one_or_none(statement)

    async def get_answer_by_question_id(self, question_id: int) -> RightAnswer | None:
        statement = select(RightAnswer).where(RightAnswer.question_id == question_id)
        return await self.one_or_none(statement)

    async def get_all_answers(self) -> Iterable[RightAnswer]:
        statement = select(RightAnswer).order_by(RightAnswer.id)
        return await self.all(statement)

    async def update_answer_by_id(self, cur_question: RightAnswer, new_question: RightAnswerSchemaIn) -> RightAnswer:

        for field, value in new_question.dict(exclude_unset=True).items():
            setattr(cur_question, field, value)

        test_res = await self.save(cur_question)
        return test_res

    async def delete_answer_by_id(self, question_id: int) -> None:
        query = delete(RightAnswer).where(RightAnswer.id == question_id)
        await self.session.execute(query)
        await self.session.commit()
