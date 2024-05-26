import requests
import sqlite3

api_key = '437e88d8'

# Function to fetch movie data
def fetch_movie_data(movie_title):
    base_url = 'http://www.omdbapi.com/'
    complete_url = f"{base_url}?t={movie_title}&apikey={api_key}"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('Response') == 'True':
            return data
        else:
            print(f"Movie '{movie_title}' not found in the database.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to store movie data in database
def store_movie_data(data):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        year TEXT,
        rated TEXT,
        released TEXT,
        runtime TEXT,
        genre TEXT,
        director TEXT,
        writer TEXT,
        actors TEXT,
        plot TEXT,
        language TEXT,
        country TEXT,
        awards TEXT,
        imdb_rating TEXT
    )
    ''')
    
    cursor.execute('''
    INSERT INTO movies (title, year, rated, released, runtime, genre, director, writer, actors, plot, language, country, awards, imdb_rating)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('Title'),
        data.get('Year'),
        data.get('Rated'),
        data.get('Released'),
        data.get('Runtime'),
        data.get('Genre'),
        data.get('Director'),
        data.get('Writer'),
        data.get('Actors'),
        data.get('Plot'),
        data.get('Language'),
        data.get('Country'),
        data.get('Awards'),
        data.get('imdbRating')
    ))
    
    conn.commit()
    conn.close()

# Main function
def main():
    # User input
    movie_title = input("Enter the movie name: ")
    
    # Fetch movie data
    data = fetch_movie_data(movie_title)
    
    if data:
        # Print movie data
        print(f"Title: {data.get('Title')}")
        print(f"Year: {data.get('Year')}")
        print(f"Rated: {data.get('Rated')}")
        print(f"Released: {data.get('Released')}")
        print(f"Runtime: {data.get('Runtime')}")
        print(f"Genre: {data.get('Genre')}")
        print(f"Director: {data.get('Director')}")
        print(f"Writer: {data.get('Writer')}")
        print(f"Actors: {data.get('Actors')}")
        print(f"Plot: {data.get('Plot')}")
        print(f"Language: {data.get('Language')}")
        print(f"Country: {data.get('Country')}")
        print(f"Awards: {data.get('Awards')}")
        print(f"IMDB Rating: {data.get('imdbRating')}")
        
        # Store movie data
        store_movie_data(data)
    else:
        print("Failed to retrieve data. Movie doesn't exist in API. Please try again.")



# Run main function
if __name__ == "__main__":
    main()
