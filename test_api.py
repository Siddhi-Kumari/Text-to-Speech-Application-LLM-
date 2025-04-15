import requests

url = "https://siddhi8825-text-to-speech-audio-application.hf.space/api/get_news_sentiment?company=Tesla"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
