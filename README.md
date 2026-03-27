# 🛡️ TruthGuard – AI Fake News Detector

🌐 **Live Web App (Streamlit Cloud):**
https://truthguard--ai.streamlit.app
Accessible via web using Streamlit Cloud deployment.

---

## 🎯 Problem Statement

Fake news spreads rapidly across digital platforms, making manual verification difficult and time-consuming.
This leads to misinformation affecting society, politics, and decision-making.

---

## 🎯 Objectives

* Classify news as **FAKE or REAL**
* Provide **clear explanation** for predictions
* Ensure **reliability** using stability testing
* Improve **awareness** about misinformation

---

## ⚙️ System Workflow

1. **User Input**

   * News text is provided by the user

2. **Preprocessing**

   * Convert to lowercase
   * Remove stopwords and special characters

3. **Machine Learning Prediction**

   * TF-IDF converts text to numerical form
   * Logistic Regression classifies news

4. **A* Keyword Analysis**

   * Identifies important and suspicious words using scoring

5. **Minimax Stability Check**

   * Tests prediction robustness by removing keywords

6. **AI Fact Verification**

   * Uses LLM to verify and explain the result

7. **Final Output**

   * Displays prediction, confidence score, keywords, stability, and explanation

---

## 🧠 Technologies Used

* Python
* Streamlit
* scikit-learn
* NLTK
* Groq API (LLaMA 3)

---

## 📊 Dataset

The model is trained using a dataset consisting of:

* Fake news articles
* Real news articles
* Approximately **44,000 entries**
* Includes both **title and text content**

---

## 📈 Model Details

* Algorithm: Logistic Regression
* Feature Extraction: TF-IDF (Unigram + Bigram)
* Accuracy: ~95–97%

---

## 🔍 Key Features

* Hybrid AI approach (ML + AI + Algorithms)
* Explainable results with reasoning
* Keyword-based analysis using A* concept
* Stability testing using Minimax concept
* User-friendly interface

---

## 🔮 Future Enhancements

* Multilingual support
* Real-time news scraping
* Mobile application
* Voice-based input

---

## 📌 Conclusion

TruthGuard provides an effective solution for detecting fake news by combining machine learning, algorithmic validation, and AI-based reasoning.
The system ensures accurate, reliable, and transparent results, helping users identify misinformation efficiently.
