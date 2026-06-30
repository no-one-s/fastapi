from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker,create_async_engine
from sqlalchemy.orm import DeclarativeBase

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_ = AsyncSession,
    expire_on_commit=False,#*this expire on commit = fales is recommended for async uses because it prevents
    #*issue with expired object after a commit, sqlalchemy would normally try to reload it lazily,
    #*but lasy loading dont work in async
)

class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session