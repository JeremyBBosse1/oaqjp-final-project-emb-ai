from flask import Flask, request, render_template
from emotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("\emotionDetector")
def emo_Detector():
    text_to_analyse = request.args('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    emotions = response[{"anger": emotion_predictions['anger'],
    "disgust": emotion_predictions['disgust'],
    "fear": emotion_predictions['fear'],
    "joy": emotion_predictions['joy'],
    "sadness": emotion_predictions['sadness'],
    "dominant_emotion": dominant_emotion}]
    return f"For the given statement, the system response is {emotions}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
