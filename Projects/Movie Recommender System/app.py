import streamlit as st
import pickle
import pandas as pd
import requests

# st.set_page_config(layout="wide")

# API_KEY = "9f8ed67b5ed6fc06ab56bff4f462bc5c" 

# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

#     try:
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()

#         data = response.json()
#         poster_path = data.get('poster_path')

#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500/" + poster_path

#     except requests.exceptions.RequestException:
#         pass

#     return "https://placehold.co/500x750?text=No+Poster"


# movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))


# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]

#     movie_list = sorted(
#         list(enumerate(distances)),
#         reverse=True,
#         key=lambda x: x[1]
#     )[1:21]

#     names = []
#     posters = []

#     for i in movie_list:
#         movie_id = movies.iloc[i[0]]['id']
#         names.append(movies.iloc[i[0]]['title'])
#         posters.append(fetch_poster(movie_id))

#     return names, posters


# st.title(" Movie Recommender System ")

# selected_movie = st.selectbox("Select a movie:", movies['title'].values)

# if st.button("Recommend"):
#     names, posters = recommend(selected_movie)

#     for start in range(0, len(names), 4):
#         cols = st.columns(4)

#         for col, name, poster in zip(
#             cols, names[start:start+4], posters[start:start+5]
#         ):
#             with col:
#                 st.write(name)
#                 st.image(poster, use_container_width=True)








# 1. Page Configuration (Must be first)
st.set_page_config(
    layout="wide", page_title="Movie Recommender System", page_icon="🎬"
)

# 2. Custom CSS styling to make cards, text, and layout look modern & sleek
st.markdown(
    """
    <style>
        /* Main background & font adjustments */
        .main {
            background-color: #0e1117;
        }
        /* Movie title styling */
        .movie-title {
            font-size: 15px;
            font-weight: 600;
            color: #ffffff;
            text-align: center;
            height: 45px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            text-overflow: ellipsis;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            margin-top: 8px;
            margin-bottom: 8px;
        }
        /* Card container styling */
        .movie-card {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s ease-in-out;
        }
        .movie-card:hover {
            transform: scale(1.02);
            border-color: #8b949e;
        }
        div.stButton > button {
            background-color: #28a745;  /* Button color (Green) */
            color: white;               /* Text color */
            border: none;
            font-weight: bold;
        }
        div.stButton > button:hover {
            background-color: #218838;  /* Color when mouse hovers over it */
            color: white;
        }
    </style>
""",
    unsafe_allow_html=True,
)

API_KEY = "9f8ed67b5ed6fc06ab56bff4f462bc5c"


# --- AUTO-DOWNLOAD SIMILARITY.PKL FROM GITHUB RELEASE (Handles >100MB files) ---
@st.cache_resource
def download_similarity_file():
  if not os.path.exists("similarity.pkl"):
    with st.spinner(
        "Downloading large recommendation model (happens only once)..."
    ):
      # Paste the direct download link from your GitHub Release here:
      url = "https://github.com/adityaraj790391-svg/machine-learning/releases/download/v1.0/similarity.pkl"

      response = requests.get(url, stream=True)
      response.raise_for_status()

      with open("similarity.pkl", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
          f.write(chunk)


# Run downloader before loading data
download_similarity_file()


# Load data efficiently using cache
@st.cache_data
def load_data():
  movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
  movies = pd.DataFrame(movies_dict)
  similarity = pickle.load(open("similarity.pkl", "rb"))
  return movies, similarity


movies, similarity = load_data()


# Fetch poster with caching
@st.cache_data
def fetch_poster(movie_id):
  url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
  try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    poster_path = data.get("poster_path")
    if poster_path:
      return "https://image.tmdb.org/t/p/w500/" + poster_path
  except requests.exceptions.RequestException:
    pass
  return "https://placehold.co/500x750?text=No+Poster"


def recommend(movie):
  movie_index = movies[movies["title"] == movie].index[0]
  distances = similarity[movie_index]

  movie_list = sorted(
      list(enumerate(distances)), reverse=True, key=lambda x: x[1]
  )[1:29]

  names = []
  posters = []

  for i in movie_list:
    movie_id = movies.iloc[i[0]]["id"]
    names.append(movies.iloc[i[0]]["title"])
    posters.append(fetch_poster(movie_id))

  return names, posters


# --- UI HEADER ---
st.markdown(
    "<h1 style='text-align: center; color: #ffffff;'>🎬 CineMatch Recommender"
    " System</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #8b949e;'>Discover your next favorite"
    " film instantly.</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

selected_movie = st.selectbox("🔍 Search or select a movie:", movies["title"].values)

if st.button("Get Recommendations", use_container_width=True):
  with st.spinner("Finding similar movies..."):
    names, posters = recommend(selected_movie)

    st.markdown("### Recommended For You:")

    # Display recommendations in a grid layout (4 columns per row)
    for start in range(0, len(names), 4):
      cols = st.columns(4)

      for col, name, poster in zip(
          cols, names[start : start + 4], posters[start : start + 4]
      ):
        with col:
          st.markdown(
              f"""
                    <div class="movie-card">
                        <img src="{poster}" style="width: 100%; border-radius: 6px; aspect-ratio: 2/3; object-fit: cover;">
                        <div class="movie-title">{name}</div>
                    </div>
                    """,
              unsafe_allow_html=True,
          )