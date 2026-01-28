from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db, create_tables
from app.models.movie import Movie
from app.models.book import Book
from app.schemas.movie import MovieCreate, MovieResponse, MovieSort, Genre
from app.schemas.book import BookCreate, BookResponse, BookSort, BookGenre

app = FastAPI(title="Movie Website API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables on startup
@app.on_event("startup")
async def startup_event():
    create_tables()

@app.post("/add", response_model=MovieResponse)
async def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    """
    Add a new movie to the database.
    """
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@app.get("/view", response_model=List[MovieResponse])
async def view_movies(
    genre: Optional[Genre] = Query(None, description="Filter by genre"),
    db: Session = Depends(get_db)
):
    """
    View all movies with optional genre filtering.
    """
    query = db.query(Movie)
    
    if genre:
        query = query.filter(Movie.genre == genre.value)
    
    movies = query.order_by(Movie.date_added.desc()).all()
    return movies

@app.get("/sort", response_model=List[MovieResponse])
async def sort_movies(
    sort_by: MovieSort = Query(..., description="Sort by field"),
    genre: Optional[Genre] = Query(None, description="Filter by genre"),
    db: Session = Depends(get_db)
):
    """
    Sort movies by specified field with optional genre filtering.
    """
    query = db.query(Movie)
    
    if genre:
        query = query.filter(Movie.genre == genre.value)
    
    if sort_by == MovieSort.DATE_ADDED:
        query = query.order_by(Movie.date_added.desc())
    elif sort_by == MovieSort.TITLE:
        query = query.order_by(Movie.title.asc())
    elif sort_by == MovieSort.IMDB_RATING:
        query = query.order_by(Movie.imdb_rating.desc() if Movie.imdb_rating is not None else Movie.date_added.desc())
    elif sort_by == MovieSort.GENRE:
        query = query.order_by(Movie.genre.asc(), Movie.title.asc())
    
    movies = query.all()
    return movies

# Book endpoints
@app.post("/books/add", response_model=BookResponse)
async def add_book(book: BookCreate, db: Session = Depends(get_db)):
    """
    Add a new book to the database.
    """
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/view", response_model=List[BookResponse])
async def view_books(
    genre: Optional[BookGenre] = Query(None, description="Filter by genre"),
    author: Optional[str] = Query(None, description="Filter by author"),
    db: Session = Depends(get_db)
):
    """
    View all books with optional genre and author filtering.
    """
    query = db.query(Book)
    
    if genre:
        query = query.filter(Book.genre == genre.value)
    
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    
    books = query.order_by(Book.date_added.desc()).all()
    return books

@app.get("/books/sort", response_model=List[BookResponse])
async def sort_books(
    sort_by: BookSort = Query(..., description="Sort by field"),
    genre: Optional[BookGenre] = Query(None, description="Filter by genre"),
    author: Optional[str] = Query(None, description="Filter by author"),
    db: Session = Depends(get_db)
):
    """
    Sort books by specified field with optional genre and author filtering.
    """
    query = db.query(Book)
    
    if genre:
        query = query.filter(Book.genre == genre.value)
    
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    
    if sort_by == BookSort.DATE_ADDED:
        query = query.order_by(Book.date_added.desc())
    elif sort_by == BookSort.TITLE:
        query = query.order_by(Book.title.asc())
    elif sort_by == BookSort.AUTHOR:
        query = query.order_by(Book.author.asc(), Book.title.asc())
    elif sort_by == BookSort.RATING:
        query = query.order_by(Book.rating.desc() if Book.rating is not None else Book.date_added.desc())
    elif sort_by == BookSort.PUBLICATION_YEAR:
        query = query.order_by(Book.publication_year.desc() if Book.publication_year is not None else Book.date_added.desc())
    
    books = query.all()
    return books

@app.get("/")
async def root():
    return {"message": "Movie Website API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)