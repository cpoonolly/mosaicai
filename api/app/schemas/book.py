# from tortoise.contrib.pydantic import pydantic_model_creator
# from ..models.book import Book

# BookPydantic = pydantic_model_creator(Book)

from datetime import datetime
from pydantic import BaseModel

class BookSchema(BaseModel):
    id: int = None
    title: str = None
    author: str = None
    ISBN: str = None
    publication_time: datetime = None
    genre: str = None
    price: float = None
    quantity: int = None
