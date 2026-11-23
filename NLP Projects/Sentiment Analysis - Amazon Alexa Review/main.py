# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, send_file
import re
from io import BytesIO
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd
import pickle

# ---------------------------
# Initialize Flask
# ---------------------------
app = Flask(__name__)

# ---------------------------
# Load Stopwords
# ---------------------------
STOPWORDS = set(stopwords.words("english"))

# ---------------------------
# Load Models (Important Path)
# ---------------------------
predictor = pickle.load(open("Models/model_xgb.pkl", "rb"))
scaler = pickle.load(open("Models/scaler.pkl", "rb"))
cv = pickle.load(open("Models/countVectorizer.pkl", "rb"))

# ---------------------------
# Home Route
# ---------------------------
@app.route("/")
def home():
    return render_template("landing.html")

# ---------------------------
# Prediction Route
# ---------------------------
@app.route("/predict", methods=["POST"])
def predict():

    # Single Text Prediction
    if request.form.get("text"):
        text_input = request.form["text"]
        result = single_prediction(text_input)
        return render_template("landing.html", prediction=result)

    # Bulk CSV Prediction
    elif "file" in request.files:
        file = request.files["file"]
        data = pd.read_csv(file)
        output_csv = bulk_prediction(data)

        return send_file(
            output_csv,
            mimetype="text/csv",
            as_attachment=True,
            download_name="Predictions.csv"
        )

# ---------------------------
# Single Prediction Function
# ---------------------------
def single_prediction(text_input):

    stemmer = PorterStemmer()

    review = re.sub("[^a-zA-Z]", " ", text_input)
    review = review.lower().split()
    review = [stemmer.stem(word) for word in review if word not in STOPWORDS]
    review = " ".join(review)

    X = cv.transform([review]).toarray()
    X = scaler.transform(X)

    prediction = predictor.predict(X)[0]

    return "Positive 😊" if prediction == 1 else "Negative 😞"

# ---------------------------
# Bulk Prediction Function
# ---------------------------
def bulk_prediction(data):

    stemmer = PorterStemmer()
    corpus = []

    for sentence in data["Sentence"]:
        review = re.sub("[^a-zA-Z]", " ", str(sentence))
        review = review.lower().split()
        review = [stemmer.stem(word) for word in review if word not in STOPWORDS]
        review = " ".join(review)
        corpus.append(review)

    X = cv.transform(corpus).toarray()
    X = scaler.transform(X)

    predictions = predictor.predict(X)

    data["Predicted Sentiment"] = [
        "Positive" if p == 1 else "Negative"
        for p in predictions
    ]

    output = BytesIO()
    data.to_csv(output, index=False)
    output.seek(0)

    return output

# ---------------------------
# Run App
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)

