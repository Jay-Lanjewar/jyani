# 🎵 Surjap — Music for Your Moment
 
Answer 8 psychology-backed questions and get genre, artist, and song recommendations powered by AI — tailored to exactly how you feel right now.
 
**[▶ Try it live →](https://your-app-link.streamlit.app)**
 
---
 
## How it works
 
Surjap scores your answers across 3 psychological axes — **Energy**, **Valence** (emotional tone), and **Social** (how connected or isolated you want to feel). These scores are sent to an LLM which returns a fresh mood name, description, genres, and 6 real song recommendations — every run is unique.
 
This mirrors how platforms like Spotify internally classify music mood.
 
## Run locally
 
```bash
git clone https://github.com/Jay-Lanjewar/surjap
cd surjap
pip install -r requirements.txt
```
 
Create a `.env` file in the project folder:
```
GEMINI_API_KEY=your_key_here
```
 
Then run:
```bash
streamlit run app.py
```
 
## Deploy your own
 
1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo → set `app.py` as entry point
4. Go to Advanced Settings → Secrets → add `GEMINI_API_KEY = "your_key"`
5. Deploy. Done.
 
---
 
Built with Python, Streamlit, and Gemini API