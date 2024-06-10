from pydantic import BaseModel


class CompletedTestsUsersSchema(BaseModel):
    id: int
    test_id: int
    user_id: int
    scores: int


class CompletedTestsUsersSchemaIn(BaseModel):
    test_id: int
    user_id: int
    scores: int = 0


class CompletedTestsUsersSchemaOut(BaseModel):
    test_id: int
    user_id: int
    scores: int


class CompletedTestsUsersScoresSchemaOut(BaseModel):
    scores: int
