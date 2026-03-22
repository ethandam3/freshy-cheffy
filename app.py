from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Load ML model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

# Gemini setup
load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

gemini = genai.GenerativeModel('gemini-2.5-flash')

SYSTEM_PROMPT = """You are Cheffy, a friendly AI assistant for Freshy Cheffy — a Long Beach platform that connects people with affordable ugly produce and helps reduce food waste. 

You help users with:
- Recipe ideas that use whole ingredients and reduce waste
- Tips on how to use ugly or imperfect produce
- Information about seasonal produce in Southern California
- Food storage tips to reduce waste at home
- Sustainability and environmental impact of food choices

Keep responses short, friendly, and practical. Always tie back to reducing food waste and eating fresh local produce. Use a warm, coastal California vibe in your tone."""

@app.route('/')
def deals():
    return send_from_directory('.', 'deals.html')

@app.route('/index')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/about')
def about():
    return send_from_directory('.', 'about.html')

@app.route('/recipes')
def recipes():
    return send_from_directory('.', 'recipes.html')

@app.route('/impact')
def impact():
    return send_from_directory('.', 'impact.html')

@app.route('/community')
def community():
    return send_from_directory('.', 'community.html')

@app.route('/bear.png')
def bear():
    return send_from_directory('.', 'bear.png')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    item = data['item']
    season = int(data['season'])
    is_ugly = int(data['is_ugly'])

    row = {'season': season, 'is_ugly': is_ugly}
    for col in columns:
        if col.startswith('item_'):
            row[col] = 1 if col == f'item_{item}' else 0

    df = pd.DataFrame([row])[columns]
    df_scaled = scaler.transform(df)
    prediction = max(0.15, model.predict(df_scaled)[0])

    return jsonify({
        'item': item,
        'predicted_price': round(float(prediction), 2),
        'is_ugly': bool(is_ugly)
    })

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    
    try:
        response = gemini.generate_content(SYSTEM_PROMPT + '\n\nUser: ' + user_message)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'reply': 'Sorry, Cheffy is taking a quick break! Try again in a moment.'}), 200

if __name__ == '__main__':
    app.run(debug=True)