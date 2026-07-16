from datetime import datetime
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import SQLModel, Session, select

from database.session import engine, get_session
from models.book import Book, BookCreate, BookUpdate

SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="Bookstore API Irene Serianai C027-01-0848/2024",
    version="1.0.0",
    description="Book Inventory API"
)


@app.post("/books", response_model=Book)
def create_book(
    book: BookCreate,
    session: Session = Depends(get_session)
):
    db_book = Book(**book.model_dump())

    session.add(db_book)
    session.commit()
    session.refresh(db_book)

    return db_book   
    
@app.get("/books", response_model=list[Book])
def list_books(
    skip: int = 0,
    limit: int = 100,
    available: Optional[bool] = None,
    session: Session = Depends(get_session)
):
    statement = select(Book)

    if available is not None:
        statement = statement.where(Book.available == available)

    books = session.exec(statement.offset(skip).limit(limit)).all()

    return books 
    
@app.get("/books/{book_id}", response_model=Book)
def get_book(
    book_id: int,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book 
    
@app.patch("/books/{book_id}", response_model=Book)
def update_book(
    book_id: int,
    book_update: BookUpdate,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    update_data = book_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(book, key, value)

    book.updated_at = datetime.utcnow()

    session.add(book)
    session.commit()
    session.refresh(book)

    return book  

@app.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    session.delete(book)
    session.commit()

    return {"message": "Book deleted successfully"}

@app.get("/books/search", response_model=list[Book])
def search_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    session: Session = Depends(get_session)
):
    statement = select(Book)

    if title:
        statement = statement.where(Book.title.contains(title))

    if author:
        statement = statement.where(Book.author.contains(author))

    books = session.exec(statement).all()

    return books

    