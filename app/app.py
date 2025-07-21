import streamlit as st
from dotenv import load_dotenv
from pipeline.pipeline import AnimeRecommendationPipeline



load_dotenv()

st.set_page_config(page_title= "Anime Recommender", layout = 'wide')

load_dotenv()

@st.cache_resource

def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("What would you like Anime be? eg.: calm anime with train station settings")

if query:
    with st.spinner("Fetching recommendations for you.."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)


