🎬 Flask Movie Recommender System

A content-based movie recommendation web application built with Flask that uses the MovieLens 20M Dataset.
It suggests movies based on their similarity to a movie entered by the user, providing an intuitive and interactive way to explore films.

📌 Features

Search for any movie in the MovieLens 20M dataset.

Get a list of similar movies instantly.

Simple, browser-based interface for quick interactions.

Works locally after setup — no internet required.

Supports a dataset of over 20 million ratings and 27,000+ movies.

View detailed information about each movie, including overview, genres, release date, runtime, and ratings.

📂 Project Structure
Flask-Movie-Recommender/
│
├─ app.py                  # Main Flask application (routes, requests, responses)
├─ recommender.py          # Movie recommendation logic (TF-IDF, cosine similarity)
├─ utils/                  # Helper scripts (optional preprocessing, CSV loading)
├─ assets/                 # CSV datasets (tmdb_5000_movies.csv, ratings.csv, etc.)
├─ templates/              # HTML templates (index.html, results.html, movie_details.html)
├─ static/                 # CSS, JavaScript, and other static assets
├─ venv/                   # Python virtual environment
├─ requirements.txt        # Python dependencies
└─ README.md               # Project documentation

🛠 Installation & Setup
1. Clone or Download the Project
git clone <your-repo-url>
cd Flask-Movie-Recommender

2. Install Dependencies

Ensure you have Python 3.8+ installed, then install the required packages:

pip install -r requirements.txt


Key packages: Flask, pandas, scikit-learn, numpy

3. Prepare the Dataset

Download the MovieLens 20M Dataset from GroupLens.

Extract the following files:

movies.csv – movie metadata

ratings.csv – user ratings

Place them inside the assets/ folder of your project directory.

🚀 Running the Application

Open a terminal in the project directory.

Start the Flask app:

python app.py


Open the local URL in your browser (default: http://127.0.0.1:5000/).

Enter a movie title in the search box to see recommendations.

🧠 How It Works

Data Loading – Loads movies and ratings from the CSV dataset.

Feature Engineering – Builds TF-IDF vectors from movie overviews and optionally other textual features like genres or keywords.

Similarity Calculation – Uses cosine similarity to find movies that are most similar in content.

Recommendation – Returns the top N similar movies and displays them on a results page.

📷 User Flow

User searches for a movie title.

System finds similar movies based on content features.

Recommended movies are displayed on a results page.

User can click a movie to view full details or return to search for another movie.

📦 Technologies Used

Flask – Backend web framework.

Pandas – Data processing and manipulation.

Scikit-learn – TF-IDF vectorization and cosine similarity computation.

HTML/CSS – Frontend interface.

MovieLens 20M Dataset – Source of movies and ratings.

🔮 Future Improvements

Implement collaborative filtering using user ratings for more personalized recommendations.

Display movie posters using APIs like TMDb.

Add pagination for large result lists.

Deploy online using Heroku, Render, or Streamlit Cloud.

Enhance UI with Bootstrap, Tailwind CSS, or Material UI.

Allow users to save favorites or create a watchlist.

🙌 Acknowledgements

MovieLens 20M Dataset by GroupLens Research.

Scikit-learn for ML tools.

Flask for the web framework and routing.