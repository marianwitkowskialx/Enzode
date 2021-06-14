from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')

settings = Settings()

DATABASE_URL = settings.db_url

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,
                            bind=engine)

Base = declarative_base()