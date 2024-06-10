from backend.test import models as test_models
from backend.question import models as question_models
from backend.answer import models as answer_models
from backend.right_answer import models as right_answer_models

from backend.db.base import Base


__all__ = (
    "Base",
    # *test_models.__all__,
    # *question_models.__all__,
    # *answer_models.__all__,
    # *right_answer_models.__all__,
)
