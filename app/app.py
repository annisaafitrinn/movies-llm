import streamlit as st
from dotenv import load_dotenv
from pipeline.pipeline import AnimeRecommendationPipeline

load_dotenv()

st.set_page_config(page_title="🎬 Movie Recommender 🍿", layout='wide')

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

# UI
st.title("🎥 What do you want to watch? 🍿")

query = st.text_input("Type your movie preferences here... e.g., thriller with forest setting 🌲🔪")

if query:
    with st.spinner("⏳ Fetching recommendations for you..."):
        response = pipeline.recommend(query)
        st.markdown("### 🎯 Recommendations")
        st.write(response)
