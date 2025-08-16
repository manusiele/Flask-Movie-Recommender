from flask import Flask, render_template, request, jsonify, url_for
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

app = Flask(__name__)

# Load movie data
# movies = pd.read_csv("assets/tmdb_5000_movies.csv")   this will bw used when the dataset has been extracted and saved in the assets folder , i had to delete them because of the github cloud upload limit
# movie_titles = 
movie_titles = movies['title'].tolist()

# TF-IDF and similarity logic (as before)
tfidf = TfidfVectorizer(stop_words='english')
movies['overview'] = movies['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(movies['overview'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Helper function
def get_recommendations(title, cosine_sim=cosine_sim):
    title = title.lower()
    movie_dict = {t.lower(): i for i, t in enumerate(movies['title'])}
    if title not in movie_dict:
        return []
    idx = movie_dict[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/suggest')
def suggest():
    query = request.args.get('q', '').lower()
    suggestions = [title for title in movie_titles if query in title.lower()]
    return jsonify(suggestions[:10])

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form.get('movie')
    recommendations = get_recommendations(movie_name)
    return render_template('results.html', movie=movie_name, recommendations=recommendations)



@app.route('/movie_details/<title>')
def movie_details(title):
    movie = movies[movies['title'] == title]
    if movie.empty:
        return f"<h2>No details found for {title}</h2><a href='{url_for('home')}'>Back</a>"

    movie_data = movie.iloc[0].to_dict()
    
    # Convert genres JSON to readable string
    import json
    try:
        genres_list = json.loads(movie_data['genres'])
        movie_data['genres'] = ', '.join([g['name'] for g in genres_list])
    except:
        movie_data['genres'] = 'N/A'

    # Convert runtime from minutes to hrs, mins
    runtime_min = int(movie_data.get('runtime', 0))  # convert to int
    hours = runtime_min // 60
    minutes = runtime_min % 60
    movie_data['runtime_formatted'] = f"{hours}h {minutes}m"

    return render_template('movie_details.html', movie=movie_data)

if __name__ == "__main__":
    app.run(debug=True)
