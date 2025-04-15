# News Sentiment & Hindi TTS Generator

## 📌 Project Overview
This application fetches news articles about a company, performs sentiment analysis, and generates an insight summary. The summary is translated into Hindi and converted into speech using TTS (Text-to-Speech). The frontend is built with **Streamlit**, and the backend uses **Flask**.

## 🚀 Features
- Fetch news articles about a company.
- Perform sentiment analysis (Positive, Negative, Neutral).
- Extract key topics from articles.
- Generate an insight summary of news sentiment.
- Translate the summary into Hindi.
- Convert the Hindi summary into an audio file (TTS).

## 🏗️ Project Structure
```
News-TTS-App/
│-- backend/
│   │-- static/                # Store generated audio files
│   │-- utils.py               # Helper functions for news fetching, sentiment, and TTS
│   │-- api.py                 # Flask API routes
│   │-- app.py                 # Main Flask application
│   │-- requirements.txt        # Dependencies for backend
│-- frontend/
│   │-- app.py                 # Streamlit frontend script
│   │-- requirements.txt        # Dependencies for frontend
│-- README.md                   # Project documentation
│-- .gitignore                   # Ignore unnecessary files

```

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```sh
git clone https://github.com/yourusername/News-TTS-App.git
cd News-TTS-App
```

### 2️⃣ Install dependencies
#### Backend
```sh
cd backend
pip install -r requirements.txt
```
#### Frontend
```sh
cd ../frontend
pip install -r requirements.txt
```

### 3️⃣ Run the backend
```sh
cd backend
python app.py
```
This starts the Flask server at `http://127.0.0.1:5000/api`.

### 4️⃣ Run the frontend
```sh
cd ../frontend
streamlit run app.py
```
This starts the Streamlit UI for interacting with the app.

## 🌍 Deployment on Hugging Face Spaces
1. Go to [Hugging Face Spaces](https://huggingface.co/spaces) and create a new Space.
2. Choose **Gradio** for backend or **Docker** if needed.
3. Connect the GitHub repository or manually upload files.
4. Ensure `setup.sh` is included to install dependencies.
5. Deploy and test the application!

## 📝 API Endpoints

### 1️⃣ Fetch News Sentiment
**Endpoint:** `/api/get_news_sentiment?company=Tesla`
**Method:** GET
**Response:**
```json
{
    "Company": "Tesla",
    "Articles": [
        {
            "Title": "Tesla stock surges",
            "Summary": "Tesla's stock is up by 10% following strong earnings.",
            "Sentiment": "Positive",
            "Topics": ["Stock Market", "Tesla"]
        }
    ],
    "Comparative Sentiment Score": {
        "Sentiment Distribution": {
            "Positive": 1,
            "Negative": 0,
            "Neutral": 0
        }
    }
}
```

### 2️⃣ Generate Insight Summary & Hindi TTS
**Endpoint:** `/api/generate_insight_summary?company=Tesla`
**Method:** GET
**Response:**
```json
{
    "insight_summary": "Tesla's recent performance has been outstanding...",
    "audio_file": "http://127.0.0.1:5000/static/Tesla_summary.mp3"
}
```

## 📌 Future Enhancements
- Improve the sentiment analysis model.
- Add multi-language support.
- Optimize TTS processing speed.
- Deploy on a cloud server for production.

---
**👨‍💻 Developed by:** SIDDHI KUMARI
**📧 Contact:** siddhikumari593@gmail.com
**🔗 GitHub:** https://github.com/Siddhi-Kumari/Text-to-Speech-Application

