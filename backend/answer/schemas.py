from typing import Optional, List

from pydantic import BaseModel, Field


class AnswerSchema(BaseModel):
    id: int
    answer1: str
    answer2: str
    answer3: Optional[str] = None
    answer4: Optional[str] = None
    answer5: Optional[str] = None
    answer6: Optional[str] = None
    answer7: Optional[str] = None
    answer8: Optional[str] = None
    answer9: Optional[str] = None
    answer10: Optional[str] = None

    question_id: int


class AnswerSchemaIn(BaseModel):
    answer1: str
    answer2: str
    answer3: Optional[str] = None
    answer4: Optional[str] = None
    answer5: Optional[str] = None
    answer6: Optional[str] = None
    answer7: Optional[str] = None
    answer8: Optional[str] = None
    answer9: Optional[str] = None
    answer10: Optional[str] = None

    question_id: int


class AnswerSchemaOut(BaseModel):
    answer1: str
    answer2: str
    answer3: Optional[str] = None
    answer4: Optional[str] = None
    answer5: Optional[str] = None
    answer6: Optional[str] = None
    answer7: Optional[str] = None
    answer8: Optional[str] = None
    answer9: Optional[str] = None
    answer10: Optional[str] = None