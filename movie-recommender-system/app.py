import bz2
import os
import pickle
import pandas as pd
import requests
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t5/p/w500/" + poster_path
    except Exception:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        
        recommended_movie_names = []
        recommended_movie_posters = []
        
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters
    except Exception as e:
        st.error(f"Error computing recommendations: {e}")
        return [], []

# UI Setup
st.header('Movie Recommender System')

movie_dict_path = os.path.join(BASE_DIR, 'movie_dict.pkl')
similarity_path = os.path.join(BASE_DIR, 'similarity_compressed.pkl')

movies_dict = pickle.load(open(movie_dict_path, 'rb'))
movies = pd.DataFrame(movies_dict) if isinstance(movies_dict, dict) else movies_dict

with bz2.BZ2File(similarity_path, 'rb') as f:
    similarity = pickle.load(f)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    with st.spinner('Fetching recommendations...'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        
        if recommended_movie_names:
            col1, col2, col3, col4, col5 = st.columns(5)
            cols = [col1, col2, col3, col4, col5]
            
            for idx, col in enumerate(cols):
                with col:
                    st.text(recommended_movie_names[idx])
                    st.image(recommended_movie_posters[idx])
