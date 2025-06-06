import streamlit as st
import pickle
import requests
import joblib  # Added for loading compressed similarity file

OMDB_API_KEY = "fa422d9b"

def fetch_movie_details_omdb(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    poster = data.get('Poster', 'https://via.placeholder.com/300x450?text=No+Image')
    plot = data.get('Plot', 'Description not available.')
    return poster, plot

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []
    for i in movie_list:
        title = movies.iloc[i[0]].title
        poster, _ = fetch_movie_details_omdb(title)
        recommended_titles.append(title)
        recommended_posters.append(poster)
    return recommended_titles, recommended_posters

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = joblib.load('similarity_compressed.joblib')  # <-- Updated to load compressed file
movie_titles = movies['title'].values

st.set_page_config(layout="wide", page_title="Movie Recommender")
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie", movie_titles, index=0)

if 'clicked_movie' not in st.session_state:
    st.session_state['clicked_movie'] = None
if 'recommended_titles' not in st.session_state:
    st.session_state['recommended_titles'] = []
if 'recommended_posters' not in st.session_state:
    st.session_state['recommended_posters'] = []

def on_recommend_click():
    st.session_state['clicked_movie'] = selected_movie
    rec_titles, rec_posters = recommend(selected_movie)
    st.session_state['recommended_titles'] = rec_titles
    st.session_state['recommended_posters'] = rec_posters

if st.button("Recommend", on_click=on_recommend_click):
    pass  # on_click handles updating session_state

def on_recommendation_click(title):
    st.session_state['clicked_movie'] = title
    rec_titles, rec_posters = recommend(title)
    st.session_state['recommended_titles'] = rec_titles
    st.session_state['recommended_posters'] = rec_posters

def show_recommendation_grid(titles, posters):
    cols = st.columns(5)
    for i in range(len(titles)):
        with cols[i]:
            st.markdown(
                """
                <style>
                div.stButton > button:first-child {
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 100%;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )
            if st.button(titles[i], key=f"rec_btn_{titles[i]}", on_click=on_recommendation_click, args=(titles[i],)):
                pass  # state updated via on_click callback

            st.image(posters[i], use_container_width=True)

if st.session_state['clicked_movie']:
    clicked_title = st.session_state['clicked_movie']

    st.markdown("---")
    st.header(f"🎥 {clicked_title}")
    poster, plot = fetch_movie_details_omdb(clicked_title)

    desc_col, img_col = st.columns([2, 1])
    with desc_col:
        st.markdown(f"**Description:** {plot}")
    with img_col:
        st.image(poster, width=200)

    st.subheader(f"More movies like **{clicked_title}**:")
    show_recommendation_grid(st.session_state['recommended_titles'], st.session_state['recommended_posters'])

else:
    st.write("Select a movie and click Recommend to see recommendations.")
