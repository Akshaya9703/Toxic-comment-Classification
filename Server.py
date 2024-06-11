from flask import Flask, render_template
from flask_socketio import SocketIO, send
import joblib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

# Load pre-trained model and vectorizer
model_path = "model.pkl"
vectorizer_path = "vectorizer.pkl"

if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
else:
    raise FileNotFoundError("Model or vectorizer file not found.")

def classify_comment(comment):
    comment_vector = vectorizer.transform([comment])
    prediction = model.predict(comment_vector)[0]
    return prediction

@app.route('/')
def index():
    return render_template('template.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    if classify_comment(msg) == 1:
        send("Toxic comment detected", broadcast=True)
    else:
        send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)


