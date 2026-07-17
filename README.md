 Bookstore API
This project is a Bookstore API developed using FastAPI and SQLModel. It connects to a PostgreSQL database and allows users to manage books in a bookstore. The API supports creating, viewing, updating, deleting, and searching for books.

 Tools Used

- Python 3.13
- FastAPI
- SQLModel
- PostgreSQL
- Uvicorn
- Docker
- Alembic
- Python Dotenv

 Project Structure
bookstore-api/
│
├── database/
│   ├── __init__.py
│   └── session.py
│
├── models/
│   ├── __init__.py
│   └── book.py
│
├── main.py
├── docker-compose.yml
├── alembic.ini
├── .env
└── README.md


 Book Details
Each book contains the following information:

- ID
- Title
- Author
- ISBN
- Published Year
- Price
- Stock
- Availability
- Created At
- Updated At

Endpoints

| Method | Endpoint | Purpose |
|---------|----------|---------|
| GET | / | Welcome message |
| POST | /books | Add a new book |
| GET | /books | View all books |
| GET | /books/{book_id} | View one book |
| PATCH | /books/{book_id} | Update a book |
| DELETE | /books/{book_id} | Delete a book |
| GET | /books/search | Search by title or author |


http://127.0.0.1:8000/docs

GitHub: https://github.com/serianaiirene24-source/bookstore-api
