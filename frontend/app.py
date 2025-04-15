import streamlit as st
import requests

# Backend API URL
BACKEND_URL = "http://127.0.0.1:5000/api"

st.title("📰 News Sentiment & Hindi TTS Generator")

# Input for company name (Fixed: Removed comma)
company = st.text_input("Enter Company Name:", "Tesla")

if st.button("Fetch News & Sentiment"):
    with st.spinner("Fetching news..."):
        response = requests.get(f"{BACKEND_URL}/get_news_sentiment?company={company}")

        if response.status_code == 200:
            data = response.json()
            st.subheader(f"📰 News for {company}")

        
            if "Articles" not in data or not data["Articles"]:
                st.warning("No articles found for this company.")
            else:
                sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}

                for article in data["Articles"]:
                    with st.expander(f"📌 {article['Title']}"):  
                        st.write(article["Summary"])
                        st.write(f"**🟢 Sentiment:** {article['Sentiment']}")
                    
                    sentiments[article["Sentiment"]] += 1

                total_articles = len(data["Articles"])

                # Sentiment Overview
                sentiment_summary = (
                    f"🔹 **Total Articles:** {total_articles}\n"
                    f"✅ **Positive:** {sentiments['Positive']}\n"
                    f"❌ **Negative:** {sentiments['Negative']}\n"
                    f"⚪ **Neutral:** {sentiments['Neutral']}"
                )

                # SECTION: Sentiment Overview
                st.markdown("## 📊 Sentiment Overview")
                st.markdown(sentiment_summary)

                # SECTION: Insight Summary (Fetched from Backend)
                st.markdown("## 🔍 Insight Summary")
                
                with st.spinner("Generating insight summary..."):
                    insight_response = requests.get(f"{BACKEND_URL}/generate_insight_summary?company={company}")

                    if insight_response.status_code == 200:
                        insight_data = insight_response.json()
                        insight_summary = insight_data["insight_summary"]
                        audio_url = insight_data["audio_file"]

                        st.write(insight_summary)

                        # SECTION: Hindi TTS for Summary
                        st.markdown("## 🎤 Hindi TTS for Summary")
                        st.audio(audio_url, format="audio/mp3")
                        st.markdown(f"[⬇️ Download Hindi Summary Audio]({audio_url})", unsafe_allow_html=True)
                    else:
                        st.error("⚠️ Failed to generate insight summary. Please try again.")
        else:
            st.error("⚠️ Failed to fetch news. Please try again.")
