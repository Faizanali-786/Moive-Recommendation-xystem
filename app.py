import pickle
import streamlit as st
import requests
import numpy
import gzip, pickle, pickletools

    
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters
import gzip, pickle, pickletools

similarity2 = gzip.open('similarity2.pkl','rb')
similarity = pickle.load(similarity2)
#similarity2.close()


movie_dict2 = gzip.open('movie_dict2.pkl','rb')
movies = pickle.load(movie_dict2)
#movie_dict2.close()

st.header('Movie Recommender System')
#movies = pickle.load(open('movie_dict.pkl','rb'))
#similarity = pickle.load(open('similarity.pkl','rb'))

movie_data = movies['title'].values
movie_list = set(movie_data)
st.write(movie_list)
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    ("Batman Begins")
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_movie_names.values[0])
        st.image(recommended_movie_posters.values[0])
    with col2:
        st.text(recommended_movie_names.values[1])
        st.image(recommended_movie_posters.values[1])

    with col3:
        st.text(recommended_movie_names.values[2])
        st.image(recommended_movie_posters.values[2])
    with col4:
        st.text(recommended_movie_names.values[3])
        st.image(recommended_movie_posters.values[3])
    with col5:
        st.text(recommended_movie_names.values[4])
        st.image(recommended_movie_posters.values[4])
