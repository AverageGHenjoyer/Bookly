from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
from src.books.service import BookService
from sqlalchemy.ext.asyncio import AsyncSession

from src.books.schemas import Book, BookUpdateModel
from src.db.main import get_session
from src.books.service import BookService

book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = book_service.get_all_books(session)
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(
    book_data: Book, session: AsyncSession = Depends(get_session)
) -> dict:
    new_book = book_service.create_book(book_data, session)
    return new_book


@book_router.get("/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")


@book_router.patch("/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            update_data = book_update_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                book[key] = value
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found.")


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return f"The book {book["title"]} has been succesfully deleted!"
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found."
        )
