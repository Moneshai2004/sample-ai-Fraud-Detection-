# api/app.py
from flask import Flask, request, jsonify
from model_loader import ModelLoader
import pandas as pd

app = Flask(__name__)
model_loader = ModelLoader()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])  # Convert the incoming data to DataFrame
    prediction = model_loader.predict(df)
    return jsonify({'is_fraud': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
    