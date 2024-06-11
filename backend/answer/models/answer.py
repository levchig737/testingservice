from db.base import Base
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Answer(Base):
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    answer1: Mapped[str] = mapped_column(String, nullable=False)
    answer2: Mapped[str] = mapped_column(String, nullable=False)
    answer3: Mapped[str] = mapped_column(String, nullable=True)
    answer4: Mapped[str] = mapped_column(String, nullable=True)
    answer5: Mapped[str] = mapped_column(String, nullable=True)
    answer6: Mapped[str] = mapped_column(String, nullable=True)
    answer7: Mapped[str] = mapped_column(String, nullable=True)
    answer8: Mapped[str] = mapped_column(String, nullable=True)
    answer9: Mapped[str] = mapped_column(String, nullable=True)
    answer10: Mapped[str] = mapped_column(String, nullable=True)

    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("question.id"))
