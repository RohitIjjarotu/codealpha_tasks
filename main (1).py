import nltk
nltk.download('punkt_tabWhat')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample FAQ Dataset (you can expand this list)
faq_data = {
    "What is the average mileage of a car?": "The average mileage of a car depends on the model, but it's typically between 20 to 30 miles per gallon.",
    "How often should I change my engine oil?": "It's recommended to change your engine oil every 5,000 to 7,500 miles.",
    "What does ABS mean in a car?": "ABS stands for Anti-lock Braking System, which helps maintain traction during emergency braking.",
    "How do I maintain my car battery?": "Regularly check the terminals for corrosion and ensure the battery is charged properly.",
    "What is the difference between petrol and diesel cars?": "Diesel engines are generally more fuel-efficient and have more torque, while petrol engines are smoother and quieter.",
    "When should I replace my tires?": "You should replace your tires every 25,000 to 50,000 miles or when the tread depth is below 2/32 of an inch.",
}

# Preprocessing
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    return ' '.join([lemmatizer.lemmatize(token) for token in tokens if token.isalpha()])

# Prepare corpus
questions = list(faq_data.keys())
answers = list(faq_data.values())
preprocessed_questions = [preprocess(q) for q in questions]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_questions)

def get_response(user_input):
    user_input_clean = preprocess(user_input)
    user_tfidf = vectorizer.transform([user_input_clean])
    similarities = cosine_similarity(user_tfidf, tfidf_matrix)
    idx = np.argmax(similarities)

    if similarities[0, idx] > 0.2:
        return answers[idx]
    else:
        return "I'm sorry, I don't have an answer for that question."

# Chat Loop
print("🚗 Car FAQ Bot: Ask me anything about cars! Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Goodbye!")
        break
    response = get_response(user_input)
    print("Bot:", response)