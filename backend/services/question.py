from answer.schemas import AnswerSchemaOut
from question.schemas import QuestionSchemaIn, QuestionSchemaWithoutAnswers, QuestionSchemaOut, QuestionSchemaInScores
from repositories.question import QuestionRepository
from repositories.test import TestRepository


from sqlalchemy.ext.asyncio import AsyncSession

from right_answer.schemas import RightAnswerSchemaOut


class QuestionService:
    def __init__(self, session: AsyncSession):
        self.repository = QuestionRepository(session)
        self.test_repository = TestRepository(session)

    async def save_question(self, test_schema: QuestionSchemaIn) -> QuestionSchemaWithoutAnswers:
        test = await self.repository.save_question(test_schema)

        question_scores = QuestionSchemaInScores(
            min_score=test.min_score, max_score=test.max_score
        )
        cur_test = await self.test_repository.get_test_by_id(test_schema.test_id)
        test_up = await self.test_repository.add_scores(cur_test, question_scores)

        return QuestionSchemaWithoutAnswers(
            id=test.id, question=test.question, min_score=test.min_score, max_score=test.max_score,
            count_answers=test.count_answers, test_id=test.test_id
        )

    async def get_all_questions(
            self
    ) -> list[QuestionSchemaWithoutAnswers]:

        tests = await self.repository.get_all_questions()
        tests_out = []

        for test in tests:
            tests_out.append(QuestionSchemaWithoutAnswers(
                id=test.id, question=test.question, min_score=test.min_score, max_score=test.max_score,
                count_answers=test.count_answers, test_id=test.test_id
            ))

        return tests_out

    async def get_questions_by_id(
        self, test_id: int
    ) -> QuestionSchemaWithoutAnswers:
        test = await self.repository.get_question_by_id(test_id)

        return QuestionSchemaWithoutAnswers(
            id=test.id, question=test.question, min_score=test.min_score, max_score=test.max_score,
            count_answers=test.count_answers, test_id=test.test_id
        )

    async def get_questions_by_id_with_answers(
        self, test_id: int
    ) -> QuestionSchemaOut:
        test = await self.repository.get_question_by_id(test_id)

        answer_schema = AnswerSchemaOut(
            answer1=test.answer.answer1, answer2=test.answer.answer2, answer3=test.answer.answer3,
            answer4=test.answer.answer4, answer5=test.answer.answer5, answer6=test.answer.answer6,
            answer7=test.answer.answer7, answer8=test.answer.answer8, answer9=test.answer.answer9,
            answer10=test.answer.answer10
        )

        right_answer_schema = RightAnswerSchemaOut(
            answer1=test.right_answer.answer1, answer2=test.right_answer.answer2, answer3=test.right_answer.answer3,
            answer4=test.right_answer.answer4, answer5=test.right_answer.answer5, answer6=test.right_answer.answer6,
            answer7=test.right_answer.answer7, answer8=test.right_answer.answer8, answer9=test.right_answer.answer9,
            answer10=test.right_answer.answer10
        )

        return QuestionSchemaOut(
            id=test.id, question=test.question, min_score=test.min_score, max_score=test.max_score,
            count_answers=test.count_answers, answer=answer_schema, right_answer=right_answer_schema,
            test_id=test.test_id
        )

    async def update_question(
            self, test_id: int, new_test: QuestionSchemaIn,
    ) -> QuestionSchemaWithoutAnswers:
        cur_test = await self.repository.get_question_by_id(test_id)

        test = await self.repository.update_question_by_id(cur_question=cur_test, new_question=new_test)

        return QuestionSchemaWithoutAnswers(
            id=test.id, question=test.question, min_score=test.min_score, max_score=test.max_score,
            count_answers=test.count_answers, test_id=test.test_id
        )

    async def delete_question_by_id(self, test_id: int) -> None:
        await self.repository.delete_question_by_id(question_id=test_id)
