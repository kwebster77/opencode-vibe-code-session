from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db, create_tables
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieResponse, MovieSort, Genre

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

@app.get("/")
async def root():
    return {"message": "Movie Website API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)