from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import FastAPI, HTTPException, Query

from tortoise import Tortoise

from .models import Book
from .schemas import BookSchema

@asynccontextmanager
async def lifespan(app: FastAPI):
    # print("Hello world")
    await Tortoise.init(
        db_url='asyncpg://test:test@db:5432/test',
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def get_test():
    return {"Hello": "World"}

@app.post("/book")
async def create_book(bookSchema: BookSchema):
    book = await Book.create(
        title=bookSchema.title,
        author=bookSchema.author,
        ISBN=bookSchema.ISBN,
        publication_time=bookSchema.publication_time,
        genre=bookSchema.genre,
        price=bookSchema.price,
        quantity=bookSchema.quantity,
    )

    return BookSchema(
        id=book.id,
        title=book.title,
        author=book.author,
        ISBN=book.ISBN,
        publication_time=book.publication_time,
        genre=book.genre,
        price=book.price,
        quantity=book.quantity,
    )

@app.get("/book/")
async def get_books(
    price_gt: float = Query(default=None),
    price_lt: float = Query(default=None),
    publication_time_gt: datetime = Query(default=None),
    publication_time_lt: datetime = Query(default=None),
    isbn=Query(default=None),
):
    filters = {}
    if price_gt:
        filters["price__gt"] = price_gt
    if price_lt:
        filters["price__lt"] = price_lt
    if publication_time_gt:
        filters["publication_time__gt"] = publication_time_gt
    if publication_time_lt:
        filters["publication_time__lt"] = publication_time_lt
    if isbn:
        filters["ISBN"] = isbn

    books = await Book.filter(**filters).all()


    return [
        BookSchema(
            id=book.id,
            title=book.title,
            author=book.author,
            ISBN=book.ISBN,
            publication_time=book.publication_time,
            genre=book.genre,
            price=book.price,
            quantity=book.quantity,
        )
        for book in books
    ]


@app.get("/book/{book_id}")
async def get_book(book_id: int):
    book = await Book.get(id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return BookSchema(
        id=book.id,
        title=book.title,
        author=book.author,
        ISBN=book.ISBN,
        publication_time=book.publication_time,
        genre=book.genre,
        price=book.price,
        quantity=book.quantity,
    )

@app.patch("/book/{book_id}")
async def patch_book(book_id: int, bookSchema: BookSchema):
    book = await Book.get(id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Item not found")

    if bookSchema.title is not None:
        book.title = bookSchema.title
    if bookSchema.author is not None:
        book.author = bookSchema.author
    if bookSchema.ISBN is not None:
        book.ISBN = bookSchema.ISBN
    if bookSchema.publication_time is not None:
        book.publication_time = bookSchema.publication_time
    if bookSchema.genre is not None:
        book.genre = bookSchema.genre
    if bookSchema.price is not None:
        book.price = bookSchema.price
    if bookSchema.quantity is not None:
        book.quantity = bookSchema.quantity
    
    await book.save()
    await book.refresh_from_db()

    return BookSchema(
        id=book.id,
        title=book.title,
        author=book.author,
        ISBN=book.ISBN,
        publication_time=book.publication_time,
        genre=book.genre,
        price=book.price,
        quantity=book.quantity,
    )

@app.delete("/book/{book_id}")
async def delete_book(book_id: int, bookSchema: BookSchema):
    book = await Book.get(id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Item not found")

    await book.delete()

    return {"msg": "ok"}



