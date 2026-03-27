import joblib
import heapq
from preprocess import clean

tfidf = joblib.load('models/tfidf.pkl')
fake_freq = joblib.load('models/fake_freq.pkl')

def get_keywords(text):
    text = clean(text)
    words = text.split()

    scores = []

    for word in words:
        g = tfidf.idf_[tfidf.vocabulary_.get(word, 0)] if word in tfidf.vocabulary_ else 0
        h = fake_freq.get(word, 0)
        f = g + h
        scores.append((f, word))

    top_words = heapq.nlargest(5, scores)
    return list(set([w for _, w in top_words]))