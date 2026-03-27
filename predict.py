import joblib
from preprocess import clean

model = joblib.load('models/model.pkl')
tfidf = joblib.load('models/tfidf.pkl')

def predict(text):
    cleaned = clean(text)
    vector = tfidf.transform([cleaned])

    pred = model.predict(vector)[0]
    prob = model.predict_proba(vector)[0]

    confidence = max(prob) * 100
    label = "REAL" if pred == 1 else "FAKE"

    return label, round(confidence, 2)