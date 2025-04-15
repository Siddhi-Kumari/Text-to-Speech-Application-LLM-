import os
import requests
from bs4 import BeautifulSoup
from newspaper import Article
import nltk
from transformers import pipeline
from gtts import gTTS
from dotenv import load_dotenv

nltk.download('punkt')

# Load environment variables
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Ensure 'static/' folder exists for TTS audio output
if not os.path.exists("static"):
    os.makedirs("static")

def fetch_news_urls(query, num_articles=10):
    """Fetch news article URLs using NewsAPI."""
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    
    if "articles" not in response:
        return []

    return [article["url"] for article in response["articles"][:num_articles]]

def extract_article_data(url):
    """Extracts the title, summary, and full text from a news article."""
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        
        return {
            "title": article.title,
            "summary": article.summary,
            "text": article.text
        }
    except Exception as e:
        print(f"Failed to extract article from {url}: {e}")
        return None

def fetch_news(query):
    """Fetch multiple news articles and extract content."""
    urls = fetch_news_urls(query)
    return [extract_article_data(url) for url in urls if url]

# Load Sentiment Analysis Model
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """Performs sentiment analysis on the text."""
    result = sentiment_pipeline(text[:512])  # Limit to 512 characters
    sentiment = result[0]["label"]

    return "Positive" if sentiment == "POSITIVE" else "Negative" if sentiment == "NEGATIVE" else "Neutral"

def fetch_news_with_sentiment(query):
    """Fetch news articles and perform sentiment analysis."""
    articles = fetch_news(query)

    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])
    
    return articles

def generate_tts(text, filename="output.mp3"):
    """Generate Hindi TTS and save as an MP3 file."""
    save_path = os.path.join("static", filename)
    tts = gTTS(text=text, lang="hi")
    tts.save(save_path)
    return os.path.abspath(save_path)
