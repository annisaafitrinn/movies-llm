# 🎬 Movie Recommendation System using Embeddings & LLMs

Welcome to movie recommender system! This project is part of my MLOps learning journey. It combines semantic search, modern embedding models, and large language models to provide intelligent and personalized movie suggestions. Built for scalability and deployed on cloud infrastructure.

---

## 📚 Background

This project was developed after completing a **Machine Learning Ops course on Udemy**.

- The original project focused on anime recommendations.
- I **customized it to recommend movies** instead, using a large-scale dataset from Kaggle.
- **Dataset**: [IMDb Movies Dataset (per genre)](https://www.kaggle.com/datasets/rajugc/imdb-movies-dataset-based-on-genre)
- I merged the genre-specific CSV files into a single dataset, adding a `genre` column.
- 📊 **Total entries**: Over **300,000 movies**!

---

## ✨ Project Highlights

- **Semantic Embeddings**:
  - Movie titles and synopses are embedded using [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) (SBERT).
- **LLM Integration**:
  - Uses **LLaMA 3.1 8B-Instant** (via [Groq](https://groq.com)) for interactive and contextual recommendations.
- **Vector Store**:
  - Embeddings are stored in **Chroma DB** for fast vector similarity search.
- **Cloud Infrastructure**:
  - Dockerized and deployed to **Google Cloud Platform (GCP)** using **Kubernetes** for scalability.

---

## ⚠️ Important Note

Due to [GitHub’s file size restrictions](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github):

- The `chroma_db/` vector store (~52MB+) is not included in the repository.
- The full preprocessed dataset (`movies.csv` ~120MB) is also excluded.

You’ll need to recreate these locally by running the preprocessing pipeline.

---

## 🚀 How It Works

1. **Preprocessing**:
   - Merges movie data across genres.
   - Embeds movie descriptions with MiniLM and stores vectors in Chroma DB.

2. **Recommendation Flow**:
   - User query → embedded → nearest movies returned based on cosine similarity.
   - Optionally enhanced with LLaMA 3.1 via Groq API.

3. **Conversational Mode**:
   - Ask for recommendations in plain language:
     > _"Give me a feel-good romcom similar to *Notting Hill* but more modern."_  
   - LLaMA helps reason about mood, themes, and genre.

---

## 🛠️ Tech Stack

| Component        | Tech Used                       |
|------------------|---------------------------------|
| Embedding Model  | `all-MiniLM-L6-v2` (SBERT)      |
| LLM              | LLaMA 3.1 8B-Instant via Groq   |
| Vector Store     |  Chroma DB                      |
| UI               | Streamlit                       |
| Deployment       | Docker, Kubernetes              |
| Cloud            | Google Cloud Platform (GCP)     |

---

## 📁 Project Structure
movies_llm/
├── chroma_db/ # Vector store (excluded from Git)
├── data/ # Raw and preprocessed data (excluded)
├── src/ # Core recommendation logic
├── app/ # Streamlit UI and endpoints
├── pipeline/ # Preprocessing and embeddings
├── config/ # LLM & DB config
├── utils/ # Helper functions
├── Dockerfile # Container definition
├── llmops-k8s.yaml # K8s deployment YAML
├── requirements.txt # Python dependencies
└── setup.py # Project setup



