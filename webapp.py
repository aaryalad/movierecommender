import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    response = requests.get(url)
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(selected_movie):
    index = movies[movies['title'] == selected_movie].index[0]
    distances = sorted(list(enumerate(similarities[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_movies_posters = []
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_list = pickle.load(open('movie_list.pkl','rb'))

similarities = pickle.load(open('similarities.pkl', 'rb'))

movies = pd.DataFrame(movies_list)
st.title('Movie Recommender')
selected_movie = st.selectbox(
    'Select a Movie for its similar recommendation.',
    movies['title'].values
)

page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
background-image:url(https://help.nflxext.com/0af6ce3e-b27a-4722-a5f0-e32af4df3045_what_is_netflix_5_en.png);
background-size:cover;
}
</style>
"""

st.markdown(page_bg_img,unsafe_allow_html=True)



if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters  = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    #for i, j in recommendations_movie, recommendations_poster:
    with st.container():

        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])

    col6, col7, col8, col9, col10 = st.columns(5)
    with st.container():

        with col6:
            st.text(recommended_movie_names[5])
            st.image(recommended_movie_posters[5])
        with col7:
            st.text(recommended_movie_names[6])
            st.image(recommended_movie_posters[6])

        with col8:
            st.text(recommended_movie_names[7])
            st.image(recommended_movie_posters[7])
        with col9:
            st.text(recommended_movie_names[8])
            st.image(recommended_movie_posters[8])
        with col10:
            st.text(recommended_movie_names[9])
            st.image(recommended_movie_posters[9])


