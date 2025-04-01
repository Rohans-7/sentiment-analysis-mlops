import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Sample dataset
data = {
    'text': [
        "I love this product!", 
        "This is the worst experience.", 
        "Amazing quality and service!", 
        "I hate it.", 
        "Not bad, could be better."
    ],
    'label': [1, 0, 1, 0, 1]  # 1: Positive, 0: Negative
}

df = pd.DataFrame(data)

# Text vectorization and model training
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(df['text'], df['label'])

# Save the trained model
joblib.dump(pipeline, 'sentiment_model.pkl')

print("Model trained and saved as sentiment_model.pkl")
