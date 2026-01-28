import React from 'react';

const BookSort = ({ sortBy, setSortBy }) => {
  const sortOptions = [
    { value: 'date_added', label: 'Date Added' },
    { value: 'title', label: 'Title' },
    { value: 'author', label: 'Author' },
    { value: 'rating', label: 'Rating' },
    { value: 'publication_year', label: 'Publication Year' }
  ];

  const handleSortChange = (e) => {
    setSortBy(e.target.value);
  };

  return (
    <div className="book-sort">
      <label htmlFor="sort-select">Sort by:</label>
      <select
        id="sort-select"
        value={sortBy}
        onChange={handleSortChange}
        className="sort-select"
      >
        {sortOptions.map(option => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
};

export default BookSort;