import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


# , sep=","

# AGREGO encoding='latin-1' para solucionar el error de Unicode
data = pd.read_csv(r"C:\DAM\DJK\spam.csv", encoding='latin-1', usecols= [0,1])

data.columns = ["label", "message"]

print("--- Vista previa ---")
print(data.head())

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(data["message"])

y = data["label"].map({"ham": 0, "spam": 1})

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n--- Precisión ---")
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

def detectar_spam(texto):
    vector = vectorizer.transform([texto])
    pred = model.predict(vector)
    if pred[0] == 1:
        return "SPAM"
    else:
        return "NO SPAM"

print("\n--- Pruebas ---")
print(detectar_spam("Win 1000€ now, click here"))
print(detectar_spam("Hola, ¿quedamos mañana?"))