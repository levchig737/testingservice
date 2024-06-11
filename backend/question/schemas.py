from typing import Optional, List

from pydantic import BaseModel, Field

from answer.schemas import AnswerSchema, AnswerSchemaOut
from right_answer.schemas import RightAnswerSchema, RightAnswerSchemaOut


class QuestionSchema(BaseModel):
    id: int
    question: str
    min_score: int
    max_score: int
    count_answers: int
    answer: Optional[AnswerSchema] = None
    right_answer: Optional[RightAnswerSchema] = None


class QuestionSchemaIn(BaseModel):
    question: str
    min_score: int
    max_score: int
    count_answers: int

    test_id: int


class QuestionSchemaWithoutAnswers(BaseModel):
    id: int
    question: str
    min_score: int
    max_score: int
    count_answers: int


class QuestionSchemaOut(BaseModel):
    id: int
    question: str
    min_score: int
    max_score: int
    count_answers: int
    answer: AnswerSchemaOut
    right_answer: RightAnswerSchemaOut


class QuestionSchemaInScores(BaseModel):
    min_score: int
    max_score: int

