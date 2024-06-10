from typing import AsyncGenerator

from backend.config import DB_HOST, DB_NAME, DB_PASS, DB_USER
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"


engine = create_async_engine(
    DATABASE_URL, max_overflow=10, pool_pre_ping=5, pool_recycle=-1, pool_size=5, pool_timeout=30
)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
        await session.commit()


class Base(DeclarativeBase):
    __allow_unmapped__ = True
