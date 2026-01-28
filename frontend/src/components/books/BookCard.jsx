import React from 'react';

const BookCard = ({ book }) => {
  return (
    <div className="book-card">
      <div className="book-header">
        <h3 className="book-title">{book.title}</h3>
        <p className="book-author">by {book.author}</p>
      </div>
      
      <div className="book-details">
        {book.genre && (
          <span className="book-genre">{book.genre}</span>
        )}
        
        {book.publication_year && (
          <span className="book-year">{book.publication_year}</span>
        )}
        
        {book.rating && (
          <div className="book-rating">
            <span className="stars">{'★'.repeat(Math.floor(book.rating))}</span>
            <span className="rating-number">{book.rating}/5</span>
          </div>
        )}
        
        {book.language && (
          <span className="book-language">{book.language}</span>
        )}
      </div>
      
      {book.summary && (
        <div className="book-summary">
          <p>{book.summary}</p>
        </div>
      )}
      
      <div className="book-footer">
        <small className="book-date">
          Added {new Date(book.date_added).toLocaleDateString()}
        </small>
      </div>
    </div>
  );
};

export default BookCard;