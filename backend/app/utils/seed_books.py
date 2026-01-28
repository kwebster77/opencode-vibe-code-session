from sqlalchemy.orm import Session
from app.database import SessionLocal, create_tables
from app.models.book import Book
from app.schemas.book import BookCreate

def create_sample_books():
    """Create sample books for testing"""
    db = SessionLocal()
    
    try:
        sample_books = [
            BookCreate(
                title="The Great Gatsby",
                author="F. Scott Fitzgerald",
                language="English",
                genre="fiction",
                rating=4.5,
                publication_year=1925,
                summary="A classic American novel set in the Jazz Age, exploring themes of wealth, love, and the American Dream."
            ),
            BookCreate(
                title="To Kill a Mockingbird",
                author="Harper Lee",
                language="English",
                genre="fiction",
                rating=4.8,
                publication_year=1960,
                summary="A powerful story of racial injustice and childhood innocence in the American South."
            ),
            BookCreate(
                title="1984",
                author="George Orwell",
                language="English",
                genre="scifi",
                rating=4.7,
                publication_year=1949,
                summary="A dystopian social science fiction novel and cautionary tale about totalitarianism."
            ),
            BookCreate(
                title="Pride and Prejudice",
                author="Jane Austen",
                language="English",
                genre="romance",
                rating=4.6,
                publication_year=1813,
                summary="A romantic novel of manners that charts the emotional development of the protagonist Elizabeth Bennet."
            ),
            BookCreate(
                title="The Hobbit",
                author="J.R.R. Tolkien",
                language="English",
                genre="fantasy",
                rating=4.7,
                publication_year=1937,
                summary="A fantasy novel about the adventures of hobbit Bilbo Baggins as he journeys to reclaim a treasure."
            ),
            BookCreate(
                title="Steve Jobs",
                author="Walter Isaacson",
                language="English",
                genre="biography",
                rating=4.3,
                publication_year=2011,
                summary="The authorized biography of Apple co-founder Steve Jobs, based on extensive interviews."
            ),
            BookCreate(
                title="The Girl with the Dragon Tattoo",
                author="Stieg Larsson",
                language="English",
                genre="mystery",
                rating=4.4,
                publication_year=2005,
                summary="A gripping psychological thriller featuring journalist Mikael Blomkvist and hacker Lisbeth Salander."
            ),
            BookCreate(
                title="Sapiens",
                author="Yuval Noah Harari",
                language="English",
                genre="nonfiction",
                rating=4.5,
                publication_year=2011,
                summary="A brief history of humankind, exploring how Homo sapiens came to dominate the world."
            )
        ]
        
        for book_data in sample_books:
            existing_book = db.query(Book).filter(Book.title == book_data.title).first()
            if not existing_book:
                db_book = Book(**book_data.dict())
                db.add(db_book)
        
        db.commit()
        print(f"Created {len(sample_books)} sample books")
        
    except Exception as e:
        print(f"Error creating sample books: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_tables()
    create_sample_books()