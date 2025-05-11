import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyDkWnq6acVgjr4J0JAouhbBo4QpIYYuYKs"

@app.route("/gemini", methods=["POST"])
def gemini_chat():
    user_message = request.json.get("message", "")
    data = {"contents": [{"parts": [{"text": user_message}]}]}

    response = requests.post(GEMINI_API_URL, json=data)
    if response.status_code == 200:
        return jsonify({"text": response.json()["candidates"][0]["content"]})
    else:
        return jsonify({"error": "API request failed"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
