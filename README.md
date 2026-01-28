# 📚 Book to Movie Finder 🎬

A Streamlit application that finds movies based on books and compares their adaptations. The app searches for the most successful movies (by IMDB rating) that are based on a given book, displays detailed information about each movie, and highlights the differences between their perceptions and adaptations.

## 🌟 Features

- **Book-based Movie Search**: Enter any book name to find movies based on it
- **Top-rated Selection**: Automatically finds the 2 highest-rated movies from IMDB
- **Detailed Movie Information**: 
  - IMDB ratings and release years
  - Movie summaries and plot descriptions
  - Director and cast information
  - Genres and runtime
  - Poster images and additional photos
- **Comparative Analysis**: 
  - Side-by-side movie comparisons
  - Rating differences and year gaps
  - Thematic differences between adaptations
  - Perception analysis highlighting how each movie approaches the source material
- **Rich Visual Display**: Movie posters, additional images, and organized layout

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Web Scraping**: BeautifulSoup4
- **HTTP Requests**: Requests
- **Data Processing**: Pandas
- **Image Handling**: PIL (Pillow)

## 📋 Requirements

- Python 3.7 or higher
- Internet connection (for IMDB scraping)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd book-to-movie-finder
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

The app will automatically open in your web browser at `http://localhost:8501`

## 📖 Usage Guide

### Basic Usage

1. **Enter a Book Name**: Type the name of any book in the input field
   - Examples: "Harry Potter", "The Lord of the Rings", "Pride and Prejudice", "The Great Gatsby"

2. **Click "Find Movies"**: The app will search IMDB for movies based on the book

3. **View Results**: 
   - See the top 2 highest-rated movies
   - View detailed information for each movie
   - Compare the adaptations side by side

### Understanding the Output

#### Movie Information
- **Poster Image**: Main movie poster
- **Rating**: IMDB rating out of 10
- **Year**: Release year
- **Director**: Movie director
- **Cast**: Main cast members (up to 3)
- **Genres**: Movie genres
- **Runtime**: Movie duration
- **Summary**: Detailed plot summary
- **Additional Images**: More movie stills and photos

#### Comparison Analysis
- **Rating Comparison**: Side-by-side ratings with difference calculation
- **Year Gap**: Time between the two adaptations
- **Thematic Differences**: Which themes are emphasized in each version
- **Perception Analysis**: How each movie approaches the source material differently

## 🔧 How It Works

### 1. Movie Search Process
- The app searches IMDB using the book name with "based on book" filter
- It parses the search results to extract movie titles, years, and ratings
- Results are sorted by rating and the top 2 are selected

### 2. Detail Extraction
- For each selected movie, the app visits its IMDB page
- It extracts comprehensive information including:
  - Plot summaries
  - Cast and crew details
  - Poster and additional images
  - Technical specifications

### 3. Comparison Algorithm
- **Rating Analysis**: Calculates rating differences
- **Temporal Analysis**: Determines year gaps between adaptations
- **Thematic Analysis**: Identifies different themes emphasized in each version
- **Perception Mapping**: Analyzes how each adaptation interprets the source material

## 🎯 Example Searches

Try these book names to see the app in action:

- **"Harry Potter"** - Compare different Harry Potter movies
- **"The Lord of the Rings"** - See Tolkien adaptations
- **"Pride and Prejudice"** - Compare classic romance adaptations
- **"The Great Gatsby"** - Different takes on Fitzgerald's masterpiece
- **"Jane Eyre"** - Gothic romance adaptations
- **"Dracula"** - Various vampire movie interpretations

## ⚠️ Important Notes

### Web Scraping Considerations
- The app uses web scraping to gather information from IMDB
- Rate limiting is implemented to avoid overwhelming IMDB servers
- If IMDB changes its structure, some features may need updates

### Data Accuracy
- Movie information is as current as IMDB's data
- Ratings and details are subject to change on IMDB
- Some movies may have incomplete information

### Performance
- Search speed depends on internet connection and IMDB response times
- Multiple image requests may take time to load
- The app includes delays between requests to be respectful to IMDB

## 🐛 Troubleshooting

### Common Issues

1. **"No movies found" Error**
   - Try a more specific book name
   - Check spelling of the book title
   - Some books may not have movie adaptations

2. **Slow Loading**
   - Check your internet connection
   - IMDB may be experiencing high traffic
   - Try refreshing the page

3. **Missing Images**
   - Some movies may not have posters available
   - Additional images may not exist for all movies
   - Check if image URLs are still valid

### Error Messages
- **"Error searching for movies"**: IMDB search failed, try again
- **"Error getting movie details"**: Individual movie page couldn't be loaded
- **Network errors**: Check internet connection

## 🔄 Updates and Maintenance

### Regular Updates Needed
- **IMDB Structure Changes**: If IMDB updates their HTML structure, scraping functions may need updates
- **API Changes**: If IMDB implements API changes, search methods may need modification
- **Dependencies**: Keep Python packages updated for security and compatibility

### Potential Improvements
- **Caching**: Add local caching to reduce IMDB requests
- **Alternative Data Sources**: Add other movie databases as backup
- **User Preferences**: Allow users to select more than 2 movies
- **Export Features**: Add ability to export comparison results

## 📄 License

This project is for educational purposes. Please respect IMDB's terms of service when using this application.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Guidelines
- Follow PEP 8 for Python code style
- Add comments for complex functions
- Include error handling for web requests
- Test with various book names

## 📞 Support

If you encounter issues or have questions:
1. Check the troubleshooting section above
2. Verify your internet connection
3. Try different book names to test functionality
4. Check if all dependencies are properly installed

## 🎬 Enjoy the App!

Discover how different filmmakers bring beloved books to life on screen. Compare adaptations, analyze interpretations, and explore the art of literary adaptation through the lens of cinema.
