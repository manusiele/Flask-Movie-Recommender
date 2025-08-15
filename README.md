# 🎬 Flask Movie Recommender System

A **Content-Based Movie Recommendation System** built with **Flask**, **Pandas**, and **Scikit-learn**.  
This app uses **TF-IDF Vectorization** and **Cosine Similarity** to recommend movies based on their **plot/overview**.

---

## 📌 Features
- 🔍 Search for any movie in the database.
- 🎯 Get **N most similar movies** based on description similarity.
- 🖥 Simple and lightweight **Flask web interface**.
- 📂 Uses the **TMDb 5000 Movies Dataset**.
- ⚡ Fast, runs locally in your browser.

---

## 📂 Project Structure
movie_recommender/
│
├── app.py # Main Flask application
├── recommender.py # Movie recommendation algorithm
├── data/
│ └── movies.csv # Dataset (TMDb movies)
├── templates/
│ ├── index.html # Search form
│ ├── results.html # Display recommendations
└── static/
└── style.css # Optional styling

yaml
Copy
Edit

---

## 🛠 Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/movie_recommender.git
cd movie_recommender
2. Install Dependencies
Make sure you have Python 3.8+ installed.

bash
Copy
Edit
pip install flask pandas scikit-learn
3. Download the Dataset
Download TMDb 5000 Movie Metadata from Kaggle:
🔗 TMDb 5000 Movie Dataset

Extract and copy tmdb_5000_movies.csv into the data/ folder.

Rename it to:

bash
Copy
Edit
data/movies.csv
🚀 Running the Application
bash
Copy
Edit
python app.py
The app will start at:

cpp
Copy
Edit
http://127.0.0.1:5000/
🧠 How It Works
Dataset Loading – Loads all movies and their overviews from movies.csv.

Text Vectorization – Converts movie overviews into numerical vectors using TF-IDF.

Similarity Computation – Calculates cosine similarity between every movie pair.

Recommendation – Finds top N movies most similar to the searched title.

📷 Screenshots
Home Page

pgsql
Copy
Edit
[ User enters movie name here ]
Results Page

diff
Copy
Edit
Recommendations for "Avatar":
- Guardians of the Galaxy
- John Carter
- Star Trek Beyond
- ...
📦 Technologies Used
Backend: Flask (Python)

Data Processing: Pandas, Scikit-learn

Frontend: HTML, CSS

Dataset: TMDb 5000 Movies Metadata (Kaggle)

🔮 Future Improvements
🎨 Add Bootstrap styling for a modern UI.

🖼 Display movie posters using TMDb API.

📊 Support collaborative filtering for user-personalized recommendations.

🔍 Add search suggestions/autocomplete.

📜 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Kaggle - TMDb 5000 Movie Dataset

Scikit-learn Documentation

Flask Documentation

yaml
Copy
Edit
