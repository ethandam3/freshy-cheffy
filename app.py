from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

@app.route('/')
def home():
    return send_from_directory('.', 'deals.html')

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