import os
from flask import Blueprint, request, jsonify
from utils import fetch_news_with_sentiment, generate_tts
from deep_translator import GoogleTranslator

api = Blueprint('api', __name__)

def translate_text(text, target_lang="hi"):
    """Translate text from English to Hindi using Google Translator."""
    return GoogleTranslator(source="auto", target=target_lang).translate(text)

@api.route('/get_news_sentiment', methods=['GET'])
def get_news_sentiment():
    """Fetch news articles with sentiment analysis, topics, and comparative sentiment score."""
    company = request.args.get('company')
    if not company:
        return jsonify({"error": "Company name is required"}), 400

    articles = fetch_news_with_sentiment(company)
    
    if not articles:
        return jsonify({"error": "No articles found"}), 404

    # Initialize sentiment distribution
    sentiment_distribution = {"Positive": 0, "Negative": 0, "Neutral": 0}

    # Process each article
    formatted_articles = []
    for article in articles:
        sentiment_distribution[article["sentiment"]] += 1

        formatted_articles.append({
            "Title": article["title"],
            "Summary": article["summary"],
            "Sentiment": article["sentiment"],
            "Topics": article.get("topics", [])  # Extract topics if available
        })

    response_data = {
        "Company": company,
        "Articles": formatted_articles,
        "Comparative Sentiment Score": {
            "Sentiment Distribution": sentiment_distribution
        }
    }

    return jsonify(response_data)

@api.route('/generate_insight_summary', methods=['GET'])
def generate_insight_summary():
    """Generate an insight summary in English and convert its Hindi translation to speech."""
    company = request.args.get('company')
    if not company:
        return jsonify({"error": "Company name is required"}), 400

    articles = fetch_news_with_sentiment(company)
    if not articles:
        return jsonify({"error": "No articles found"}), 404

    # Generate English Insight Summary
    insight_summary_en = " ".join(article["summary"] for article in articles)[:500]

    # Translate insight summary to Hindi for TTS
    insight_summary_hi = translate_text(insight_summary_en, "hi")

    # Generate Hindi TTS from translated summary
    audio_filename = f"{company}_summary.mp3"
    audio_file_path = generate_tts(insight_summary_hi, audio_filename)

    return jsonify({
        "insight_summary": insight_summary_en,  # Display English summary
        "audio_file": f"http://127.0.0.1:5000/static/{audio_filename}"  # Hindi TTS of the translated summary
    })
