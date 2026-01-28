import streamlit as st
import requests
import re
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import pandas as pd
from urllib.parse import quote
import time

class MovieFinder:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.base_url = "https://www.imdb.com"
    
    def search_movies_by_book(self, book_name: str) -> List[Dict]:
        """Search for movies based on a book name"""
        search_query = f"{book_name} based on book"
        search_url = f"{self.base_url}/find?q={quote(search_query)}&s=tt&ttype=ft"
        
        try:
            response = requests.get(search_url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            movies = []
            result_items = soup.find_all('div', class_='ipc-metadata-list-summary-item')
            
            for item in result_items[:10]:  # Get top 10 results
                try:
                    title_elem = item.find('h3', class_='ipc-title__text')
                    if title_elem:
                        title = title_elem.text.strip()
                        
                        # Extract year
                        year_elem = item.find('span', class_='sc-b189961a-8')
                        year = year_elem.text.strip() if year_elem else "Unknown"
                        
                        # Extract rating
                        rating_elem = item.find('span', class_='ipc-rating-star')
                        rating = rating_elem.text.strip().split()[0] if rating_elem else "0.0"
                        
                        # Get movie URL
                        link_elem = item.find('a', href=True)
                        movie_url = self.base_url + link_elem['href'] if link_elem else None
                        
                        movies.append({
                            'title': title,
                            'year': year,
                            'rating': float(rating) if rating.replace('.', '').isdigit() else 0.0,
                            'url': movie_url
                        })
                except Exception as e:
                    continue
            
            # Sort by rating and return top 2
            movies.sort(key=lambda x: x['rating'], reverse=True)
            return movies[:2]
            
        except Exception as e:
            st.error(f"Error searching for movies: {str(e)}")
            return []
    
    def get_movie_details(self, movie_url: str) -> Dict:
        """Get detailed information about a movie"""
        if not movie_url:
            return {}
        
        try:
            response = requests.get(movie_url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Get summary
            summary_elem = soup.find('span', {'data-testid': 'plot-xl'})
            summary = summary_elem.text.strip() if summary_elem else "Summary not available"
            
            # Get poster image
            poster_elem = soup.find('img', {'data-testid': 'hero-media__poster'})
            poster_url = poster_elem.get('src') if poster_elem else None
            
            # Get director, cast, genre
            details = {}
            
            # Director
            director_elem = soup.find('a', {'data-testid': 'title-pc-principal-credit'})
            if director_elem:
                details['director'] = director_elem.text.strip()
            
            # Cast
            cast_elements = soup.find_all('a', {'data-testid': 'title-cast-item__actor'})
            if cast_elements:
                details['cast'] = [elem.text.strip() for elem in cast_elements[:3]]
            
            # Genre
            genre_elements = soup.find_all('a', {'data-testid': 'genres'})
            if genre_elements:
                details['genres'] = [elem.text.strip() for elem in genre_elements]
            
            # Runtime
            runtime_elem = soup.find('div', {'data-testid': 'title-techspec_runtime'})
            if runtime_elem:
                details['runtime'] = runtime_elem.text.strip()
            
            return {
                'summary': summary,
                'poster_url': poster_url,
                'details': details
            }
            
        except Exception as e:
            st.error(f"Error getting movie details: {str(e)}")
            return {}
    
    def get_additional_images(self, movie_url: str) -> List[str]:
        """Get additional movie images"""
        if not movie_url:
            return []
        
        try:
            photos_url = movie_url.replace('/reference/', '/mediaindex/')
            response = requests.get(photos_url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            images = []
            img_elements = soup.find_all('img', src=True)
            
            for img in img_elements[:5]:  # Get first 5 images
                src = img.get('src')
                if src and 'media' in src and '.jpg' in src:
                    images.append(src)
            
            return images
            
        except Exception as e:
            return []

def compare_movies(movie1: Dict, movie2: Dict) -> Dict:
    """Compare two movies and highlight differences"""
    comparison = {
        'ratings': {
            'movie1': movie1.get('rating', 0),
            'movie2': movie2.get('rating', 0),
            'difference': abs(movie1.get('rating', 0) - movie2.get('rating', 0))
        },
        'years': {
            'movie1': movie1.get('year', 'Unknown'),
            'movie2': movie2.get('year', 'Unknown'),
            'gap': None
        },
        'themes': [],
        'styles': []
    }
    
    # Calculate year gap
    try:
        year1 = int(movie1.get('year', '0'))
        year2 = int(movie2.get('year', '0'))
        comparison['years']['gap'] = abs(year1 - year2)
    except:
        pass
    
    # Extract themes from summaries
    summary1 = movie1.get('details', {}).get('summary', '').lower()
    summary2 = movie2.get('details', {}).get('summary', '').lower()
    
    # Common themes to look for
    themes = ['love', 'war', 'adventure', 'mystery', 'family', 'friendship', 'betrayal', 'redemption']
    
    for theme in themes:
        theme_in_1 = theme in summary1
        theme_in_2 = theme in summary2
        
        if theme_in_1 != theme_in_2:
            comparison['themes'].append({
                'theme': theme,
                'in_movie1': theme_in_1,
                'in_movie2': theme_in_2
            })
    
    return comparison

def main():
    st.set_page_config(
        page_title="Book to Movie Finder",
        page_icon="📚🎬",
        layout="wide"
    )
    
    st.title("📚 Book to Movie Finder 🎬")
    st.markdown("Enter a book name to find the most successful movies based on it and compare their adaptations.")
    
    # Initialize movie finder
    movie_finder = MovieFinder()
    
    # User input
    book_name = st.text_input("Enter Book Name:", placeholder="e.g., Harry Potter, The Lord of the Rings, Pride and Prejudice")
    
    if st.button("Find Movies") and book_name:
        with st.spinner("Searching for movies..."):
            movies = movie_finder.search_movies_by_book(book_name)
            
            if not movies:
                st.warning("No movies found based on the entered book name. Please try a different book.")
                return
            
            st.success(f"Found {len(movies)} movie(s) based on '{book_name}'")
            
            # Get detailed information for each movie
            detailed_movies = []
            for movie in movies:
                details = movie_finder.get_movie_details(movie['url'])
                movie.update(details)
                detailed_movies.append(movie)
                time.sleep(1)  # Rate limiting
            
            # Display movies
            for i, movie in enumerate(detailed_movies, 1):
                st.subheader(f"🎬 Movie {i}: {movie['title']}")
                
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    if movie.get('poster_url'):
                        st.image(movie['poster_url'], caption=f"{movie['title']}", use_column_width=True)
                    else:
                        st.write("📷 No poster available")
                
                with col2:
                    st.write(f"**⭐ Rating:** {movie['rating']}/10")
                    st.write(f"**📅 Year:** {movie['year']}")
                    
                    if movie.get('details', {}).get('director'):
                        st.write(f"**🎭 Director:** {movie['details']['director']}")
                    
                    if movie.get('details', {}).get('cast'):
                        st.write(f"**👥 Cast:** {', '.join(movie['details']['cast'])}")
                    
                    if movie.get('details', {}).get('genres'):
                        st.write(f"**🎪 Genres:** {', '.join(movie['details']['genres'])}")
                    
                    if movie.get('details', {}).get('runtime'):
                        st.write(f"**⏱️ Runtime:** {movie['details']['runtime']}")
                
                st.write("**📖 Summary:**")
                st.write(movie.get('summary', 'Summary not available'))
                
                # Additional images
                additional_images = movie_finder.get_additional_images(movie['url'])
                if additional_images:
                    st.write("**🖼️ Additional Images:**")
                    cols = st.columns(min(len(additional_images), 3))
                    for idx, img_url in enumerate(additional_images[:3]):
                        with cols[idx]:
                            st.image(img_url, use_column_width=True)
                
                st.divider()
            
            # Comparison section
            if len(detailed_movies) == 2:
                st.subheader("🔍 Movie Comparison")
                comparison = compare_movies(detailed_movies[0], detailed_movies[1])
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        f"{detailed_movies[0]['title']} Rating",
                        f"{comparison['ratings']['movie1']}/10"
                    )
                
                with col2:
                    st.metric("Rating Difference", f"{comparison['ratings']['difference']:.1f}")
                
                with col3:
                    st.metric(
                        f"{detailed_movies[1]['title']} Rating",
                        f"{comparison['ratings']['movie2']}/10"
                    )
                
                # Year comparison
                if comparison['years']['gap']:
                    st.write(f"**📅 Year Gap:** {comparison['years']['gap']} years between adaptations")
                
                # Theme differences
                if comparison['themes']:
                    st.write("**🎭 Thematic Differences:**")
                    for theme_diff in comparison['themes']:
                        movie_indicator = "✅" if theme_diff['in_movie1'] else "❌"
                        movie2_indicator = "✅" if theme_diff['in_movie2'] else "❌"
                        st.write(f"- **{theme_diff['theme'].title()}:** {detailed_movies[0]['title']} {movie_indicator}, {detailed_movies[1]['title']} {movie2_indicator}")
                
                # Perception analysis
                st.write("**🧠 Perception Analysis:**")
                st.write(f"- **{detailed_movies[0]['title']}** ({comparison['years']['movie1']}): {'Higher rated' if comparison['ratings']['movie1'] > comparison['ratings']['movie2'] else 'Lower rated'} adaptation focusing on {', '.join([t['theme'] for t in comparison['themes'] if t['in_movie1']]) if comparison['themes'] else 'similar themes'}.")
                st.write(f"- **{detailed_movies[1]['title']}** ({comparison['years']['movie2']}): {'Higher rated' if comparison['ratings']['movie2'] > comparison['ratings']['movie1'] else 'Lower rated'} adaptation focusing on {', '.join([t['theme'] for t in comparison['themes'] if t['in_movie2']]) if comparison['themes'] else 'similar themes'}.")

if __name__ == "__main__":
    main()