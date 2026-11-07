import streamlit as st
import pickle
import pandas as pd
import requests

API_KEY = "9f8ed67b5ed6fc06ab56bff4f462bc5c" 

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

    except requests.exceptions.RequestException:
        pass

    return "https://placehold.co/500x750?text=No+Poster"


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    names = []
    posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]]['id']
        names.append(movies.iloc[i[0]]['title'])
        posters.append(fetch_poster(movie_id))

    return names, posters


st.title("Movie Recommender System")

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    for start in range(0, len(names), 5):
        cols = st.columns(5)

        for col, name, poster in zip(
            cols, names[start:start+5], posters[start:start+5]
        ):
            with col:
                st.write(name)
                st.image(poster)