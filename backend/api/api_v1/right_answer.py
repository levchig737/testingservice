from typing import Annotated

from fastapi import APIRouter, Depends
from backend.right_answer.schemas import RightAnswerSchema, RightAnswerSchemaIn
from backend.services.right_answer import RightAnswerService

from backend.api.deps import get_right_answer_service


router = APIRouter()

RightAnswerServiceDeps = Annotated[RightAnswerService, Depends(get_right_answer_service)]


@router.post("/")
async def create_answer(
    new_test: RightAnswerSchemaIn, service: RightAnswerServiceDeps
) -> RightAnswerSchemaIn:
    return await service.save_answer(new_test)


@router.get("/", response_model=list[RightAnswerSchemaIn])
async def get_all_right_answers(
    service: RightAnswerServiceDeps
) -> list[RightAnswerSchemaIn]:

    return await service.get_all_answers()


@router.get("/{answer_id}/", response_model=RightAnswerSchemaIn)
async def get_right_answer_by_id(
    answer_id: int, service: RightAnswerServiceDeps
) -> RightAnswerSchemaIn:

    return await service.get_answer_by_id(answer_id)


@router.get("/question/{question_id}/", response_model=RightAnswerSchemaIn)
async def get_answer_by_question_id(
    question_id: int, service: RightAnswerServiceDeps
) -> RightAnswerSchemaIn:

    return await service.get_answer_by_question_id(question_id)


@router.patch("/{answer_id}/", response_model=RightAnswerSchemaIn)
async def update_right_answer(
        answer_id: int, new_test: RightAnswerSchemaIn, service: RightAnswerServiceDeps
) -> RightAnswerSchemaIn:
    return await service.update_answer(answer_id, new_test)


@router.delete("/{answer_id}/", response_model=None)
async def delete(answer_id: int, service: RightAnswerServiceDeps) -> None:

    return await service.delete_answer_by_id(answer_id)
