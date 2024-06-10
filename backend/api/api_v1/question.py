from typing import Annotated

from fastapi import APIRouter, Depends
from backend.question.schemas import QuestionSchemaIn, QuestionSchemaWithoutAnswers, QuestionSchemaOut
from backend.services.question import QuestionService

from backend.api.deps import get_question_service


router = APIRouter()

QuestionServiceDeps = Annotated[QuestionService, Depends(get_question_service)]


@router.post("/")
async def create_question(
    new_test: QuestionSchemaIn, service: QuestionServiceDeps
) -> QuestionSchemaWithoutAnswers:
    return await service.save_question(new_test)


@router.get("/", response_model=list[QuestionSchemaWithoutAnswers])
async def get_all_questions(
    service: QuestionServiceDeps
) -> list[QuestionSchemaWithoutAnswers]:

    return await service.get_all_questions()


@router.get("/without_answers/{question_id}/", response_model=QuestionSchemaWithoutAnswers)
async def get_question_by_id(
    question_id: int, service: QuestionServiceDeps
) -> QuestionSchemaWithoutAnswers:

    return await service.get_questions_by_id(question_id)


@router.get("/with_answers/{question_id}/", response_model=QuestionSchemaOut)
async def get_question_by_id(
    question_id: int, service: QuestionServiceDeps
) -> QuestionSchemaOut:

    return await service.get_questions_by_id_with_answers(question_id)


@router.patch("/{question_id}/", response_model=QuestionSchemaWithoutAnswers)
async def update_question(
        question_id: int, new_test: QuestionSchemaIn, service: QuestionServiceDeps
) -> QuestionSchemaWithoutAnswers:
    return await service.update_question(question_id, new_test)


@router.delete("/{question_id}/", response_model=None)
async def delete(question_id: int, service: QuestionServiceDeps) -> None:

    return await service.delete_question_by_id(question_id)
