from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum


class Genre(str, Enum):
    ACTION = "action"
    COMEDY = "comedy"
    DRAMA = "drama"
    HORROR = "horror"
    ROMANCE = "romance"
    SCIFI = "scifi"
    THRILLER = "thriller"
    DOCUMENTARY = "documentary"
    ANIMATION = "animation"
    FANTASY = "fantasy"


class MovieBase(BaseModel):
    title: str
    language: str = "English"
    summary: Optional[str] = None
    trailer_url: Optional[str] = None
    genre: Optional[Genre] = None
    imdb_rating: Optional[float] = None


class MovieCreate(MovieBase):
    pass


class MovieResponse(MovieBase):
    id: int
    date_added: datetime
    
    class Config:
        from_attributes = True


class MovieSort(str, Enum):
    DATE_ADDED = "date_added"
    TITLE = "title"
    IMDB_RATING = "imdb_rating"
    GENRE = "genre"