import React from 'react';

const BookFilter = ({ filters, setFilters }) => {
  const bookGenres = [
    'fiction', 'nonfiction', 'mystery', 'romance', 
    'scifi', 'fantasy', 'thriller', 'biography', 
    'history', 'selfhelp'
  ];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilters(prev => ({
      ...prev,
      [name]: value
    }));
  };

  return (
    <div className="book-filter">
      <div className="filter-group">
        <label htmlFor="author-filter">Author:</label>
        <input
          id="author-filter"
          type="text"
          name="author"
          value={filters.author}
          onChange={handleChange}
          placeholder="Search by author..."
          className="filter-input"
        />
      </div>
      
      <div className="filter-group">
        <label htmlFor="genre-filter">Genre:</label>
        <select
          id="genre-filter"
          name="genre"
          value={filters.genre}
          onChange={handleChange}
          className="filter-select"
        >
          <option value="">All Genres</option>
          {bookGenres.map(genre => (
            <option key={genre} value={genre}>
              {genre.charAt(0).toUpperCase() + genre.slice(1)}
            </option>
          ))}
        </select>
      </div>
      
      <button
        className="clear-filters"
        onClick={() => setFilters({ genre: '', author: '' })}
      >
        Clear Filters
      </button>
    </div>
  );
};

export default BookFilter;