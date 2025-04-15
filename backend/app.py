from flask import Flask, jsonify
from flask_cors import CORS
from api import api

app = Flask(__name__)
CORS(app)

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def home():
    return jsonify({"message": "Flask API is running. Use /api/get_news_sentiment?company=Tesla"})

if __name__ == '__main__':
    app.run(debug=True)
