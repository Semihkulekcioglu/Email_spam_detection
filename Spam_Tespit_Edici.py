import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Veriyi oku
df = pd.read_csv('spam_ham_dataset.csv')
df = df.drop(columns=['Unnamed: 0'])

# Temizleme fonksiyonu
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df['clean_text'] = df['text'].apply(clean_text)

# Eğitim/test ayrımı
X = df['clean_text']
y = df['label_num']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Değerlendirme
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=['Ham', 'Spam']))

# Tahmin fonksiyonu
def predict_spam(text):
    clean = clean_text(text)
    vector = vectorizer.transform([clean])
    prediction = model.predict(vector)[0]
    return "SPAM 🚨" if prediction == 1 else "HAM (normal) 📩"

# Test
if __name__ == "__main__":
    while True:
        sample = input("\nE-posta metnini gir (çıkmak için q):\n")
        if sample.lower() == 'q':
            break
        print("→ Tahmin:", predict_spam(sample))
