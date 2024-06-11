from test import models as test_models
from question import models as question_models
from answer import models as answer_models
from right_answer import models as right_answer_models

from db.base import Base


__all__ = (
    "Base",
    # *test_models.__all__,
    # *question_models.__all__,
    # *answer_models.__all__,
    # *right_answer_models.__all__,
)
