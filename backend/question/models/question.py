from backend.db.base import Base
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


class Question(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question: Mapped[str] = mapped_column(String)
    min_score: Mapped[int] = mapped_column(Integer)
    max_score: Mapped[int] = mapped_column(Integer)
    count_answers: Mapped[int] = mapped_column(Integer)

    answer = relationship('Answer', backref='question', uselist=False)

    right_answer = relationship('RightAnswer', backref='question', uselist=False)

    test_id: Mapped[int] = mapped_column(Integer, ForeignKey("test.id"))
