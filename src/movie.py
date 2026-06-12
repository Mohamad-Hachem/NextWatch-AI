from pydantic import BaseModel, Field
from typing import Optional


class Movie:
    id: int
    title: str
    author: str
    category:str
    description: str
    rating: int

    def __init__(self, id, title, author, category, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.description = description
        self.rating = rating


class MovieRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    category:str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=-1, lt=6)