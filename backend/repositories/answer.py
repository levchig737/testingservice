from typing import Iterable

from db.base_repository import BaseRepository
from answer.models.answer import Answer
from answer.schemas import AnswerSchema, AnswerSchemaIn
from sqlalchemy import delete, select


class AnswerRepository(BaseRepository):
    async def save_answer(self, test: AnswerSchemaIn) -> Answer:
        result = await self.save(Answer(**test.model_dump()))
        return result

    async def get_answer_by_id(self, question_id: int) -> Answer | None:
        statement = select(Answer).where(Answer.id == question_id)
        return await self.one_or_none(statement)

    async def get_answer_by_question_id(self, question_id: int) -> Answer | None:
        statement = select(Answer).where(Answer.question_id == question_id)
        return await self.one_or_none(statement)

    async def get_all_answers(self) -> Iterable[Answer]:
        statement = select(Answer).order_by(Answer.id)
        return await self.all(statement)

    async def update_answer_by_id(self, cur_question: Answer, new_question: AnswerSchemaIn) -> Answer:

        for field, value in new_question.dict(exclude_unset=True).items():
            setattr(cur_question, field, value)

        test_res = await self.save(cur_question)
        return test_res

    async def delete_answer_by_id(self, question_id: int) -> None:
        query = delete(Answer).where(Answer.id == question_id)
        await self.session.execute(query)
        await self.session.commit()
