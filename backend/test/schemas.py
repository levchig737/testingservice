from typing import List

from pydantic import BaseModel

from question.schemas import QuestionSchemaOut


class TestSchema(BaseModel):
    id: int
    name: str
    owner: str
    theme: str
    min_score: int
    max_score: int

    questions: List[QuestionSchemaOut] = []


class TestSchemaIn(BaseModel):
    name: str
    owner: str
    theme: str


class TestSchemaOut(BaseModel):
    id: int
    name: str
    owner: str
    theme: str
    min_score: int
    max_score: int

    questions: List[QuestionSchemaOut] = []


class TestSchemaWithoutQuestions(BaseModel):
    id: int
    name: str
    owner: str
    theme: str
    min_score: int
    max_score: int


class TestSchemaInScores(BaseModel):
    min_score: int
    max_score: int


class TestSchemaCount(BaseModel):
    count: int


class TestSchemaAverageResult(BaseModel):
    id: int
    average_result: float
