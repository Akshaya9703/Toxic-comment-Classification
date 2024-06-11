from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Sample comments
comments = ["Hi",
    "Great job! Keep up the good work",
    "This is really insightful, thank you for sharing",
    "You have a great perspective on this topic",
    "I appreciate your contribution to the discussion",
    "You're very talented!",
    "Thank you for your hard work",
    "You made a difference with your comment",
    "That's a brilliant idea!",
    "I agree with your point completely",
    "You're doing amazing things!",
    "I like you",
    "You're a complete piece of trash",
    "Go fuck yourself",
    "You are such a worthless idiot",
    "Everyone hates you, just die already",
    "You're a disgusting human being",
    "Nobody cares about your stupid opinions",
    "You're nothing but a pathetic loser",
    "Why don't you just kill yourself?",
    "You're a waste of oxygen",
    "I hope you suffer for the rest of your life",
    "i hate you"
]

# Labels for the comments (positive or negative sentiment)
labels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Create a CountVectorizer to convert text into a matrix of token counts
vectorizer = CountVectorizer(lowercase=True)
X = vectorizer.fit_transform(comments)

# Create a Logistic Regression model
model = LogisticRegression()
model.fit(X, labels)

# Save the model and vectorizer to disk
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)
