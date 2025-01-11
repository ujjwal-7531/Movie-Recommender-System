import streamlit as st
import pickle as pk
import pandas as pd
import requests
import time

df = pk.load(open('/home/ujjwal/Programs/ML-DS/PROJECTS/Movie Reccomender System/movie_list.pkl','rb'))
similarity = pk.load(open('/home/ujjwal/Programs/ML-DS/PROJECTS/Movie Reccomender System/similarity.pkl','rb'))
# df = pk.load(open('movie_list.pkl','rb'))
# similarity = pk.load(open('similarity.pkl','rb'))


# fetching movie poster based on movie id
def fetch_poster(movie_id):
    res = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=4883dd9047e6e5bc8cc5f77e00e9232f".format(movie_id))
    data = res.json()
    return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]


# recommender function
def recommender(movie):
    index = df[df["title"]==movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[0:5] 
    
    recommendedMovies = []
    posters =[]
    
    for i in movies_list:
        recommendedMovies.append(df.iloc[i[0]].title)
        posters.append(fetch_poster(df.iloc[i[0]].movie_id))
    return recommendedMovies, posters

        
        
        
st.title("🎥 Movie Reccomender")

movies_list = df.title.values
selected_movie = st.selectbox("What are you looking for ?", movies_list)

if st.button('Recommend'):

    names, posters = recommender(selected_movie)
    c1,c2,c3,c4,c5 = st.columns(5)
    
    with st.spinner("Loading..."):
        time.sleep(3)
    
    with c1:
        st.image(posters[0])
        st.write(names[0])
    with c2:
        st.image(posters[1])
        st.write(names[1])
    with c3:
        st.image(posters[2])
        st.write(names[2])
    with c4:
        st.image(posters[3])
        st.write(names[3])
    with c5:
        st.image(posters[4])
        st.write(names[4])
        





        
        
        
        