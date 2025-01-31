import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv( )
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("POSTGRES_DB")
url = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"
engine = create_async_engine(url, echo=True)

async def get_alchemy_session():
    async with engine.begin() as conn:
        await conn.run_sync( Base.metadata.create_all )
    Session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    yield Session()
    Session.close_all()

Base = declarative_base()
