from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from datetime import datetime
from app.database import Base


class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False, index=True)
    language = Column(String, default="English")
    summary = Column(Text, nullable=True)
    genre = Column(String, nullable=True, index=True)
    rating = Column(Float, nullable=True)
    publication_year = Column(Integer, nullable=True)
    date_added = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"