import pandas as pd

# first make sure you have extracted the TMDB 5000 Movie Dataset.zip and save it at the assets folder to get the two .csv files
movies = pd.read_csv("../assets/tmdb_5000_movies.csv")
credits = pd.read_csv("../assets/tmdb_5000_credits.csv")

print(movies.shape)
print(credits.shape)
movies = movies.merge(credits, left_on='id', right_on='movie_id', how='inner')
print(movies.shape)
