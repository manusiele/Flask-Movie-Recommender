🎬 Flask Movie Recommender System

A content-based movie recommendation web application built with Flask that uses the MovieLens 20M Dataset.
It suggests movies based on their similarity to a movie entered by the user.

📌 Features

Search for any movie in the MovieLens 20M dataset.

Get a list of similar movies instantly.

Simple, browser-based interface.

Works locally after setup — no internet needed.

Supports a dataset of over 20 million ratings and 27,000+ movies.

📂 Project Structure

Main Application File – Handles routes, requests, and responses.

Algorithm File – Contains the movie recommendation logic.

Dataset Folder – Contains MovieLens CSV files (movies.csv, ratings.csv, etc.).

Templates Folder – HTML files for the web interface.

Static Folder – CSS, images, and other assets.

🛠 Installation & Setup
1. Clone or Download the Project

Get the project files from your repository or ZIP archive.

2. Install Dependencies

Ensure you have Python installed, then install required packages such as
Flask, Pandas, and Scikit-learn.

3. Prepare the Dataset

Download the MovieLens 20M Dataset from GroupLens:
🔗 MovieLens 20M Dataset

From the downloaded ZIP file:

Extract movies.csv (movie metadata) and ratings.csv (user ratings).

Place them inside the data folder in your project directory.

🚀 Running the Application

Open a terminal in the project directory.

Start the Flask application.

Open the provided local URL in your browser.

Enter a movie title in the search box to see recommendations.

🧠 How It Works

Data Loading – The app loads movies and ratings from the dataset.

Feature Engineering – Builds feature vectors from genres or aggregated user preferences.

Similarity Calculation – Uses cosine similarity to find the most similar movies.

Recommendation – Displays the top N similar movies to the one entered.

📷 User Flow

Step 1: User searches for a movie title.

Step 2: System finds similar movies based on content features and/or user ratings.

Step 3: Similar movies are displayed on a results page.

Step 4: User can return to search for another movie.

📦 Technologies Used

Flask – Backend web framework.

Pandas – Data processing.

Scikit-learn – Similarity computation.

HTML/CSS – Frontend.

MovieLens 20M Dataset – Source of movies and ratings.

🔮 Future Improvements

Implement collaborative filtering using user ratings for more personalized results.

Display movie posters via an API like TMDb.

Add pagination for large result lists.

Deploy online using Heroku, Render, or Streamlit Cloud.

Enhance UI with Bootstrap or Tailwind CSS.

🙌 Acknowledgements

MovieLens 20M Dataset by GroupLens Research.

Scikit-learn for machine learning tools.

Flask for the web framework.
