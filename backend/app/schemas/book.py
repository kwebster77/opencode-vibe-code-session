from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum


class BookGenre(str, Enum):
    FICTION = "fiction"
    NONFICTION = "nonfiction"
    MYSTERY = "mystery"
    ROMANCE = "romance"
    SCIFI = "scifi"
    FANTASY = "fantasy"
    THRILLER = "thriller"
    BIOGRAPHY = "biography"
    HISTORY = "history"
    SELFHELP = "selfhelp"


class BookBase(BaseModel):
    title: str
    author: str
    language: str = "English"
    summary: Optional[str] = None
    genre: Optional[BookGenre] = None
    rating: Optional[float] = None
    publication_year: Optional[int] = None


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int
    date_added: datetime
    
    class Config:
        from_attributes = True


class BookSort(str, Enum):
    DATE_ADDED = "date_added"
    TITLE = "title"
    AUTHOR = "author"
    RATING = "rating"
    PUBLICATION_YEAR = "publication_year"