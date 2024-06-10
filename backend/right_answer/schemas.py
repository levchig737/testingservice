from typing import Optional, List

from pydantic import BaseModel, Field


class RightAnswerSchema(BaseModel):
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


class RightAnswerSchemaIn(BaseModel):
    answer1: bool
    answer2: Optional[bool] = None
    answer3: Optional[bool] = None
    answer4: Optional[bool] = None
    answer5: Optional[bool] = None
    answer6: Optional[bool] = None
    answer7: Optional[bool] = None
    answer8: Optional[bool] = None
    answer9: Optional[bool] = None
    answer10: Optional[bool] = None

    question_id: int


class RightAnswerSchemaOut(BaseModel):
    answer1: bool
    answer2: Optional[bool] = None
    answer3: Optional[bool] = None
    answer4: Optional[bool] = None
    answer5: Optional[bool] = None
    answer6: Optional[bool] = None
    answer7: Optional[bool] = None
    answer8: Optional[bool] = None
    answer9: Optional[bool] = None
    answer10: Optional[bool] = None
