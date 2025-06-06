# Movie Recommender System 🎬

Welcome to the Movie Recommender System — a simple, interactive web app built with Streamlit that recommends movies based on a selected title. It fetches movie details and posters dynamically from the OMDb API and uses a precomputed similarity matrix for recommendations.

---

## 🔍 Project Description

This project uses collaborative filtering based on a similarity matrix of movies to recommend similar titles to users. The core features include:

- Select a movie from a dropdown list.
- Get top 5 recommended movies similar to the selected one.
- View movie posters and detailed descriptions fetched live from the OMDb API.
- Interactive UI built with Streamlit.
- Handles large similarity matrix download on-demand from Google Drive to avoid large repo size.

The recommender is designed to be lightweight, user-friendly, and deployable on Streamlit Cloud.

---

## 🌐 Live Demo:

You can try out the app live here:

[https://movie-recommender-jhlslnfon2l2vdarqhmt7x.streamlit.app/](https://movie-recommender-jhlslnfon2l2vdarqhmt7x.streamlit.app/)

---

## 📁 Repository Contents

- `app.py` — Main Streamlit app script.
- `movies.pkl` — Pickled movie metadata file.
- `similarity_compressed.joblib` — Compressed similarity matrix (not included in repo; downloaded on app startup).
- `requirements.txt` — Python dependencies.

---

## ⚙️ Setup & Installation

Follow these steps to run the app locally:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender

# 2. Create a Python virtual environment
python3 -m venv venv

# 3. Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1

# 4. Install required packages
pip install -r requirements.txt

# 5. Run the Streamlit app
streamlit run app.py

```
## 🔧 Dependencies

This project uses the following Python libraries:

- `streamlit` — Web app framework for building the interactive UI.  
- `joblib` — For loading the precomputed similarity matrix.  
- `pickle` — For loading the movie metadata (`movies.pkl`).  
- `requests` — To fetch poster and plot data from the OMDb API.  
- `gdown` — To download the similarity matrix file from Google Drive.

---

## 🎯 How It Works

- **Data**  
  Uses a precomputed similarity matrix (`similarity_compressed.joblib`) hosted on Google Drive, along with a small metadata file (`movies.pkl`) containing movie titles.

- **Selection**  
  The user selects a movie from the dropdown menu.

- **Recommendation**  
  Based on the selected movie, the top 5 most similar movies are recommended using the similarity matrix.

- **Details**  
  Poster and plot details for each recommended movie are fetched in real-time from the OMDb API.

- **UI**  
  Movies are displayed in a 5-column grid with clickable buttons. Clicking a recommended movie will show further recommendations related to it, allowing recursive discovery.

---

## 📝 Notes

- 🔑 Keep your OMDb API key in `app.py`. The current key used is `"fa422d9b"`. You can obtain your own free key from [OMDb API](https://www.omdbapi.com/apikey.aspx).

- ⬇️ The similarity matrix file is **not included** in the GitHub repo (to keep it lightweight). It will be downloaded automatically from Google Drive the first time the app runs.

- 🌐 Ensure you have an **active internet connection** for:
  - Downloading the similarity matrix on first run.
  - Fetching real-time data (posters and plots) from OMDb.

- 🛠️ Feel free to customize and enhance the app! Ideas include:
  - Adding search filters
  - Switching to TMDB API
  - Using collaborative filtering models

---


