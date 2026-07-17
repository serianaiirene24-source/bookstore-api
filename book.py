from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, min_length=1)
    author: str = Field(index=True, min_length=1)
    isbn: str = Field(index=True, unique=True)
    published_year: int = Field(ge=1000, le=datetime.now().year)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    available: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class BookCreate(SQLModel):
    title: str
    author: str
    isbn: str
    published_year: int
    price: float
    stock: int
    available: bool = True


class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    published_year: Optional[int] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    available: Optional[bool] = None