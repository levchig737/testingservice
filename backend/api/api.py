from fastapi import APIRouter
from starlette.responses import JSONResponse

from api.api_v1.test import router as test_router
from api.api_v1.question import router as question_router
from api.api_v1.answer import router as answer_router
from api.api_v1.right_answer import router as right_answer_router
from api.api_v1.user import router as user_router
from api.api_v1.completed_tests_users import router as completed_tests_users_router


router = APIRouter()

router.include_router(test_router, prefix="/test", tags=["test"])
router.include_router(question_router, prefix="/question", tags=["question"])
router.include_router(answer_router, prefix="/answer", tags=["answer"])
router.include_router(right_answer_router, prefix="/right_answer", tags=["right_answer"])
router.include_router(completed_tests_users_router, prefix="/completed_test", tags=["completed_test"])
router.include_router(user_router)


@router.get("/check_startup/")
async def check_startup() -> JSONResponse:
    return JSONResponse(status_code=204, content=None)
