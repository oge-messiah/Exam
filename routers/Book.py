from fastapi import APIRouter
from schemas.BookSchema import BookBase


router = APIRouter()

Books = [
    BookBase(title="The Alchemist", author="Paulo Coelho", id="BG202", is_available=True),
    BookBase(title="The Hobbit", author="J.R.R. Tolkien", id= "BG605", is_available=False),
    BookBase(title="The GingerMan", author="JP Donleavy", id= "BG700", is_available=True),
    BookBase(title="Angels & Demons", author="Dan Brown", id= "BG707", is_available=False),
    BookBase(title="Harry Porter", author="JK Rowling", id= "BG953", is_available=True),
    BookBase(title="Things fall apart", author="Chinua Achebe", id= "BG999", is_available=False),
]


@router.get("/")
def get_all_books():
    return Books 


@router.get("/{book_id}")
def get_book_by_id(book_id: str):
    return next((book for book in Books if book.id == book_id), None)

@router.post("/")
def create_book(book: BookBase):
    Books.append(book)
    return {"message": "Book added successfully", "Data": book}

@router.put("/{book_id}")
def update_book(book_id: str, book: BookBase):
    book_to_update = next((book for book in Books if book.id == book_id), None)
    if book_to_update:
        book_to_update.title = book.title
        book_to_update.author = book.author
        return book_to_update
    return None

@router.delete("/{book_id}")
def delete_book(book_id: str):
    book_to_delete = next((book for book in Books if book.id == book_id), None)
    if book_to_delete:
        Books.remove(book_to_delete)
        return {"message": "Book deleted successfully"}
    return None





