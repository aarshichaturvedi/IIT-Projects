import streamlit as st
import pickle # to export import data
import pandas as pd
import requests


def fetch_poster(movie_id):
   response = requests.get( "https://api.themoviedb.org/3/movie/{}?api_key=be828e8f723d2b50a0c264306bd6749b&language=en-US".format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# function to recommend a movie
def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # same as above

        recommended_movies = []
        recommended_movies_posters = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].id

            recommended_movies.append(movies.iloc[i[0]].title)   # this will return the top 5 similar movies with their titles

            # fetch the poster of the movie from the API using movie_id
            recommended_movies_posters.append(fetch_poster(movie_id))
        return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movies Arena 🍿')
st.subheader('-Aarshi Chaturvedi')

# adding textbox to type the movie name
movie_name = st.selectbox(
    'Search for your favourite movie 🎬: ', movies['title'].values)


# creating a button
if st.button("Recommend 5 similar movies! ", type="primary" , icon= "⭐"):
    names,posters = recommend(movie_name)


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

# music so we don't get bored
st.subheader(" Music meanwhile 🎸!!")

st.audio("happyrock.mp3", format="audio/mpeg", loop=True)

