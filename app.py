from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

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

if __name__ == '__main__':
    app.run(debug=True)