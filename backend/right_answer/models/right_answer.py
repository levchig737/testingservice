from backend.db.base import Base
from sqlalchemy import ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


class RightAnswer(Base):
    __tablename__ = "right_answer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    answer1: Mapped[bool] = mapped_column(Boolean, nullable=False)
    answer2: Mapped[bool] = mapped_column(Boolean, nullable=True)
    answer3: Mapped[bool] = mapped_column(Boolean, nullable=True)
    answer4: Mapped[bool] = mapped_column(Boolean, nullable=True)
    answer5: Mapped[bool] = mapped_column(Boolean, nullable=True)
    answer6: Mapped[bool] = mapped_column(Boolean, nullable=True)
    answer7: Mapped[bool] = mapped_column(Boolean, nullable=True)
    answer8: Mapped[bool] = mapped_column(Boolean, nullable=True)
    answer9: Mapped[bool] = mapped_column(Boolean, nullable=True)
    answer10: Mapped[bool] = mapped_column(Boolean, nullable=True)

    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("question.id"))
