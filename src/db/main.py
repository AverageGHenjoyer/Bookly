from sqlmodel import create_engine, text, SQLModel 
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import Config

engine = AsyncEngine(
            create_engine(
                        url=Config.DATABASE_URL,
                        echo=True 
                        ))

async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=async_session,
        class=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session
        