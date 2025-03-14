"""
server.py

Flask application for detecting emotions in text.
This API provides an endpoint to analyze the emotional content of user-provided text.

Author: Jeremy Bosse
Date: 3/14/2025
"""
from flask import Flask, request, render_template
from emotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emo_detector():
    """Endpoint to analyze the emotion of a given text"""
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!", 400
    return f"The given text has been identified as {dominant_emotion}"

@app.route("/")
def render_index_page():
    """Render the home page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
