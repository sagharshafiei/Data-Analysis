import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# recommended system

imdb = pd.read_csv("imdb_top_1000.csv")


df = imdb[["Series_Title", "Genre", "Director", "Star1", "Star2", "Star3", "Star4"]]
df["CombinedFeatures"] = df["Genre"] + " " + df["Director"] + " "+ df["Star1"]+ " " + df["Star2"]+ " " + df["Star3"]+ " " + df["Star4"]
# df.info()

vectorizer = CountVectorizer(stop_words="english")
features_vectors = vectorizer.fit_transform(df["CombinedFeatures"])


# fav = input("Enter Your Favorite Movie : ")
fav = "The Godfather"
idx = (df[df["Series_Title"] == fav].index)[0]

similarities = cosine_similarity(features_vectors, features_vectors[idx])

movies = np.c_[df["Series_Title"], similarities]

num_recommended = 5

recommended = sorted(movies, key=lambda movie: movie[1], reverse=True)
print(np.array(recommended)[1:num_recommended+1, 0])

