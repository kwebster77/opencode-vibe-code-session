import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const bookService = {
  // Get all books with optional filters and sorting
  getBooks: async (endpoint = 'view', params = '') => {
    try {
      const response = await axios.get(`${API_BASE_URL}/books/${endpoint}${params ? `?${params}` : ''}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching books:', error);
      throw error;
    }
  },

  // Add a new book
  addBook: async (bookData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/books/add`, bookData);
      return response.data;
    } catch (error) {
      console.error('Error adding book:', error);
      throw error;
    }
  },

  // Get sorted books
  getSortedBooks: async (sortBy, filters = {}) => {
    const params = new URLSearchParams();
    params.append('sort_by', sortBy);
    
    if (filters.genre) params.append('genre', filters.genre);
    if (filters.author) params.append('author', filters.author);
    
    return await bookService.getBooks('sort', params.toString());
  }
};

export { bookService };