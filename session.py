import os
from pathlib import Path

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set.")

engine = create_engine(
    DATABASE_URL,
    echo=True,
)


def get_session():
    with Session(engine) as session:
        yield session