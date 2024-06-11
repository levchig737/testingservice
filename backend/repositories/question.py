from typing import Iterable

from sqlalchemy.orm import joinedload

from db.base_repository import BaseRepository
from question.models.question import Question
from question.schemas import QuestionSchemaIn
from sqlalchemy import delete, select


class QuestionRepository(BaseRepository):
    async def save_question(self, test: QuestionSchemaIn) -> Question:
        result = await self.save(Question(**test.model_dump()))
        return result

    async def get_question_by_id(self, question_id: int) -> Question | None:
        statement = (
            select(Question)
            .options(joinedload(Question.answer), joinedload(Question.right_answer))
            .where(Question.id == question_id)
        )
        return await self.one_or_none(statement)

    async def get_all_questions(self) -> Iterable[Question]:
        statement = select(Question).order_by(Question.id)
        return await self.all(statement)

    async def get_answers(self) -> Iterable[Question]:
        statement = select(Question.answer).order_by(Question.id)
        return await self.all(statement)

    async def get_right_answers(self) -> Iterable[Question]:
        statement = select(Question.right_answer).order_by(Question.id)
        return await self.all(statement)

    async def update_question_by_id(self, cur_question: Question, new_question: QuestionSchemaIn) -> Question:

        for field, value in new_question.dict(exclude_unset=True).items():
            setattr(cur_question, field, value)

        test_res = await self.save(cur_question)
        return test_res

    async def delete_question_by_id(self, question_id: int) -> None:
        query = delete(Question).where(Question.id == question_id)
        await self.session.execute(query)
        await self.session.commit()
