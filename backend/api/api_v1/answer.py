from typing import Annotated

from fastapi import APIRouter, Depends
from answer.schemas import AnswerSchemaIn
from services.answer import AnswerService

from api.deps import get_answer_service


router = APIRouter()

AnswerServiceDeps = Annotated[AnswerService, Depends(get_answer_service)]


@router.post("/")
async def create_answer(
    new_test: AnswerSchemaIn, service: AnswerServiceDeps
) -> AnswerSchemaIn:
    return await service.save_answer(new_test)


@router.get("/", response_model=list[AnswerSchemaIn])
async def get_all_answers(
    service: AnswerServiceDeps
) -> list[AnswerSchemaIn]:

    return await service.get_all_answers()


@router.get("/{answer_id}/", response_model=AnswerSchemaIn)
async def get_answer_by_id(
    answer_id: int, service: AnswerServiceDeps
) -> AnswerSchemaIn:

    return await service.get_answer_by_id(answer_id)


@router.get("/question/{question_id}/", response_model=AnswerSchemaIn)
async def get_answer_by_question_id(
    question_id: int, service: AnswerServiceDeps
) -> AnswerSchemaIn:

    return await service.get_answer_by_question_id(question_id)


@router.patch("/{answer_id}/", response_model=AnswerSchemaIn)
async def update_answer(
        answer_id: int, new_test: AnswerSchemaIn, service: AnswerServiceDeps
) -> AnswerSchemaIn:
    return await service.update_answer(answer_id, new_test)


@router.delete("/{answer_id}/", response_model=None)
async def delete(answer_id: int, service: AnswerServiceDeps) -> None:

    return await service.delete_answer_by_id(answer_id)