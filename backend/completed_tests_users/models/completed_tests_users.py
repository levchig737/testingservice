from db.base import Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class CompletedTestsUsers(Base):
    __tablename__ = "completed_tests_users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    test_id: Mapped[int] = mapped_column(Integer, ForeignKey("test.id"))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    scores: Mapped[int] = mapped_column(Integer, nullable=False)
