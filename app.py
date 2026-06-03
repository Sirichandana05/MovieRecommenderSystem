import streamlit as st
import pandas as pd
import pickle

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# UI
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Show Recommendations"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(movie)

