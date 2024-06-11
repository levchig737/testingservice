from right_answer.schemas import RightAnswerSchemaIn
from repositories.right_answer import RightAnswerRepository
from repositories.question import QuestionRepository

from sqlalchemy.ext.asyncio import AsyncSession


def replace_none_with_false(data: dict) -> dict:
    return {k: (v if v is not None else False) for k, v in data.items()}


class RightAnswerService:
    def __init__(self, session: AsyncSession):
        self.repository = RightAnswerRepository(session)
        self.question_repository = QuestionRepository(session)

    async def save_answer(self, test_schema: RightAnswerSchemaIn) -> RightAnswerSchemaIn:
        test = await self.repository.save_answer(test_schema)

        # Считаем кол-во введенных ответов
        non_null_answers_count = sum(answer is not None for answer in test_schema.dict().values()) - 1

        question = await self.question_repository.get_question_by_id(test_schema.question_id)

        # Проверяем соответствие кол-ва ответов
        # if non_null_answers_count != question.count_answers:
        #     raise HTTPException(status_code=400, detail=
        #     f"Кол-во ответов: {non_null_answers_count} не соответствует кол-ву вопросов в ответе: {question.count_answers}")

        return RightAnswerSchemaIn(
                answer1=test.answer1, answer2=test.answer2, answer3=test.answer3,
                answer4=test.answer4, answer5=test.answer5, answer6=test.answer6,
                answer7=test.answer7, answer8=test.answer8, answer9=test.answer9,
                answer10=test.answer10, question_id=test.question_id
            )

    async def get_answer_by_id(
        self, test_id: int
    ) -> RightAnswerSchemaIn:
        test = await self.repository.get_answer_by_id(test_id)

        return RightAnswerSchemaIn(
            answer1=test.answer1, answer2=test.answer2, answer3=test.answer3,
            answer4=test.answer4, answer5=test.answer5, answer6=test.answer6,
            answer7=test.answer7, answer8=test.answer8, answer9=test.answer9,
            answer10=test.answer10, question_id=test.question_id
        )

    async def get_answer_by_question_id(
        self, test_id: int
    ) -> RightAnswerSchemaIn:
        test = await self.repository.get_answer_by_question_id(test_id)

        return RightAnswerSchemaIn(
            answer1=test.answer1, answer2=test.answer2, answer3=test.answer3,
            answer4=test.answer4, answer5=test.answer5, answer6=test.answer6,
            answer7=test.answer7, answer8=test.answer8, answer9=test.answer9,
            answer10=test.answer10, question_id=test.question_id
        )

    async def get_all_answers(
            self
    ) -> list[RightAnswerSchemaIn]:

        tests = await self.repository.get_all_answers()
        tests_out = []

        for test in tests:
            tests_out.append(RightAnswerSchemaIn(
                answer1=test.answer1, answer2=test.answer2, answer3=test.answer3,
                answer4=test.answer4, answer5=test.answer5, answer6=test.answer6,
                answer7=test.answer7, answer8=test.answer8, answer9=test.answer9,
                answer10=test.answer10, question_id=test.question_id
            ))

        return tests_out

    async def update_answer(
            self, test_id: int, new_test: RightAnswerSchemaIn,
    ) -> RightAnswerSchemaIn:
        cur_test = await self.repository.get_answer_by_id(test_id)

        test = await self.repository.update_answer_by_id(cur_question=cur_test, new_question=new_test)

        return RightAnswerSchemaIn(
            answer1=test.answer1, answer2=test.answer2, answer3=test.answer3,
            answer4=test.answer4, answer5=test.answer5, answer6=test.answer6,
            answer7=test.answer7, answer8=test.answer8, answer9=test.answer9,
            answer10=test.answer10, question_id=test.question_id
        )

    async def delete_answer_by_id(self, test_id: int) -> None:
        await self.repository.delete_answer_by_id(question_id=test_id)
