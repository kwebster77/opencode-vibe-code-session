import React, { useState, useEffect } from 'react';
import BookCard from './BookCard';
import BookFilter from './BookFilter';
import BookSort from './BookSort';
import { bookService } from '../../services/bookService';

const BookList = () => {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filters, setFilters] = useState({
    genre: '',
    author: ''
  });
  const [sortBy, setSortBy] = useState('date_added');

  const fetchBooks = async () => {
    try {
      setLoading(true);
      const params = new URLSearchParams();
      
      if (filters.genre) params.append('genre', filters.genre);
      if (filters.author) params.append('author', filters.author);
      if (sortBy !== 'date_added') params.append('sort_by', sortBy);
      
      const endpoint = sortBy === 'date_added' ? 'view' : 'sort';
      const data = await bookService.getBooks(endpoint, params.toString());
      setBooks(data);
    } catch (err) {
      setError('Failed to fetch books');
      console.error('Error fetching books:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchBooks();
  }, [filters, sortBy]);

  if (loading) return <div>Loading books...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="book-list">
      <div className="book-controls">
        <BookFilter filters={filters} setFilters={setFilters} />
        <BookSort sortBy={sortBy} setSortBy={setSortBy} />
      </div>
      
      <div className="books-grid">
        {books.length === 0 ? (
          <div className="no-books">No books found</div>
        ) : (
          books.map(book => (
            <BookCard key={book.id} book={book} />
          ))
        )}
      </div>
    </div>
  );
};

export default BookList;