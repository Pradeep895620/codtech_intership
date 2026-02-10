import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 1. Use a slightly larger dummy dataset
data = {
    'text': [
        'get free coins now', 'hi how are you', 'win a prize today', 
        'meeting at five', 'cash prize winner', 'let us go for lunch',
        'exclusive deal for you', 'can you send the file', 'claim your gift',
        'the report is ready'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] # 1=Spam, 0=Ham
}
df = pd.DataFrame(data)

# 2. Split Data - Added random_state for consistency
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.3, random_state=42
)

# 3. Vectorize
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# 4. Train
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# 5. Predict
predictions = model.predict(X_test_counts)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
print(f"Predictions: {predictions}")
print(f"Actual Labels: {y_test.values}")
