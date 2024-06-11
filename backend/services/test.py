from fastapi import HTTPException

from answer.schemas import AnswerSchemaOut
from right_answer.schemas import RightAnswerSchemaOut
from test.schemas import TestSchemaIn, TestSchemaOut, TestSchemaWithoutQuestions, TestSchemaCount, \
    TestSchemaAverageResult
from question.schemas import QuestionSchemaOut
from repositories.test import TestRepository
from repositories.question import QuestionRepository
from repositories.answer import AnswerRepository
from repositories.right_answer import RightAnswerRepository
from repositories.completed_tests_users import CompletedTestsUsersRepository

from sqlalchemy.ext.asyncio import AsyncSession


async def validate_blocked_user(blocked_flag: bool) -> bool:
    return blocked_flag


class TestService:
    def __init__(self, session: AsyncSession):
        self.repository = TestRepository(session)
        self.question_repository = QuestionRepository(session)
        self.answer_repository = AnswerRepository(session)
        self.right_answer_repository = RightAnswerRepository(session)
        self.completed_test_repository = CompletedTestsUsersRepository(session)

    async def save_test(self, test_schema: TestSchemaIn) -> TestSchemaWithoutQuestions:
        test = await self.repository.save_test(test_schema)

        return TestSchemaWithoutQuestions(
            id=test.id, name=test.name, owner=test.owner, theme=test.theme, min_score=test.min_score,
            max_score=test.max_score
        )

    async def get_all_tests(
            self, blocked_flag: bool
    ) -> list[TestSchemaWithoutQuestions]:

        if await validate_blocked_user(blocked_flag):
            raise HTTPException(status_code=400, detail="USER_BLOCKED")

        tests = await self.repository.get_all_tests()
        tests_out = []

        for test in tests:
            tests_out.append(TestSchemaWithoutQuestions(
                id=test.id, name=test.name, owner=test.owner, theme=test.theme, min_score=test.min_score,
                max_score=test.max_score
            ))

        return tests_out

    async def get_tests_count(
            self
    ) -> TestSchemaCount:
        count = await self.repository.get_tests_count()
        return TestSchemaCount(
            count=count
        )

    async def get_test_by_id(
        self, test_id: int
    ) -> TestSchemaWithoutQuestions:
        test = await self.repository.get_test_by_id(test_id)

        return TestSchemaWithoutQuestions(
            id=test.id, name=test.name, owner=test.owner, theme=test.theme, min_score=test.min_score,
            max_score=test.max_score
        )

    async def get_test_by_id_with_questions(
            self, test_id: int, blocked_flag: bool
    ) -> TestSchemaOut:
        test = await self.repository.get_test_by_id(test_id)

        if await validate_blocked_user(blocked_flag):
            raise HTTPException(status_code=400, detail="USER_BLOCKED")

        if test is None:
            raise ValueError(f"Test with id {test_id} not found")

        new_questions = []
        for question in test.questions:
            question_id = question.id
            answer = await self.answer_repository.get_answer_by_question_id(question_id)
            right_answer = await self.right_answer_repository.get_answer_by_question_id(question_id)

            # Преобразование ответа и правильного ответа в схемы Pydantic
            answer_schema = AnswerSchemaOut(
                answer1=answer.answer1, answer2=answer.answer2, answer3=answer.answer3,
                answer4=answer.answer4, answer5=answer.answer5, answer6=answer.answer6,
                answer7=answer.answer7, answer8=answer.answer8, answer9=answer.answer9,
                answer10=answer.answer10
            ) if answer else None
            right_answer_schema = RightAnswerSchemaOut(
                answer1=right_answer.answer1, answer2=right_answer.answer2, answer3=right_answer.answer3,
                answer4=right_answer.answer4, answer5=right_answer.answer5, answer6=right_answer.answer6,
                answer7=right_answer.answer7, answer8=right_answer.answer8, answer9=right_answer.answer9,
                answer10=right_answer.answer10
            ) if right_answer else None

            question_schema = QuestionSchemaOut(
                id=question.id,
                question=question.question,
                min_score=question.min_score,
                max_score=question.max_score,
                count_answers=question.count_answers,
                answer=answer_schema,
                right_answer=right_answer_schema
            )
            new_questions.append(question_schema)

        if not new_questions:
            raise HTTPException(status_code=400, detail=f"No questions found for test {test.id}")

        return TestSchemaOut(
            id=test.id,
            name=test.name,
            owner=test.owner,
            theme=test.theme,
            min_score=test.min_score,
            max_score=test.max_score,
            questions=new_questions
        )

    async def get_test_by_theme(
            self, theme: str
    ) -> list[TestSchemaWithoutQuestions]:

        tests = await self.repository.get_tests_by_theme(theme)
        tests_out = []

        for test in tests:
            tests_out.append(TestSchemaWithoutQuestions(
                id=test.id, name=test.name, owner=test.owner, theme=test.theme, min_score=test.min_score,
                max_score=test.max_score
            ))

        return tests_out

    async def get_average_result_users(
        self, test_id: int
    ) -> TestSchemaAverageResult:
        completed_tests = await self.completed_test_repository.get_all_completed_tests_users_by_test_id(test_id)

        # Пробежаться по всем тестам и получить средний результат
        average_result = 0.0
        for test in completed_tests:
            average_result += test.scores

        average_result /= len(completed_tests)
        average_result = round(average_result, 2)

        return TestSchemaAverageResult(
            id=test_id, average_result=average_result
        )

    async def update_test(
            self, test_id: int, new_test: TestSchemaIn,
    ) -> TestSchemaWithoutQuestions:
        cur_test = await self.repository.get_test_by_id(test_id)

        test = await self.repository.update_test_by_id(cur_test=cur_test, new_test=new_test)

        return TestSchemaWithoutQuestions(
            id=test.id, name=test.name, owner=test.owner, theme=test.theme, min_score=test.min_score,
            max_score=test.max_score
        )

    async def delete_test_by_id(self, test_id: int) -> None:
        test = await self.repository.get_test_by_id(test_id)
        for i in range(len(test.questions)):
            question = await self.question_repository.get_question_by_id(test.questions[i].id)

            answer = await self.answer_repository.get_answer_by_question_id(question.id)
            right_answer = await self.right_answer_repository.get_answer_by_question_id(question.id)

            # Удаление ответов
            if answer != None:
                await self.answer_repository.delete_answer_by_id(answer.id)
            if right_answer != None:
                await self.right_answer_repository.delete_answer_by_id(right_answer.id)

            # Удаление вопроса
            await self.question_repository.delete_question_by_id(question.id)

        await self.repository.delete_test_by_id(test_id=test_id)
