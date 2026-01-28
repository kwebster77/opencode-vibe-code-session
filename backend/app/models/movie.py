from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from datetime import datetime
from app.database import Base


class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    language = Column(String, default="English")
    summary = Column(Text, nullable=True)
    trailer_url = Column(String, nullable=True)
    genre = Column(String, nullable=True, index=True)
    imdb_rating = Column(Float, nullable=True)
    date_added = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}', genre='{self.genre}')>"