import pandas as pd
from preprocess import clean
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from collections import Counter

# Load data
fake = pd.read_csv('data/Fake.csv')
true = pd.read_csv('data/True.csv')

fake['label'] = 0
true['label'] = 1

# Merge + SHUFFLE 🔥
df = pd.concat([fake, true]).sample(frac=1).reset_index(drop=True)

# Clean text
df['text'] = df['text'].apply(clean)

# TF-IDF IMPROVED 🔥
tfidf = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
X = tfidf.fit_transform(df['text'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Better model 🔥
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Accuracy check
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(model, 'models/model.pkl')
joblib.dump(tfidf, 'models/tfidf.pkl')

# Fake word frequency (A*)
fake_words = " ".join(df[df['label'] == 0]['text']).split()
fake_freq_dict = dict(Counter(fake_words))

joblib.dump(fake_freq_dict, 'models/fake_freq.pkl')

print("✅ Training complete")
