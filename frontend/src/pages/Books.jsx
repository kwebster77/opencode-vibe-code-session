import React from 'react';
import BookList from '../components/books/BookList';

const Books = () => {
  return (
    <div className="books-page">
      <header className="page-header">
        <h1>Books Library</h1>
        <p>Browse and discover your next favorite book</p>
      </header>
      
      <main className="page-content">
        <BookList />
      </main>
    </div>
  );
};

export default Books;