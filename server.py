"""Flask web application for emotion detection."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    """Render the homepage with the emotion detection form."""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """Analyze the statement and return the formatted response."""
    statement = request.args.get('textToAnalyze')
    result = emotion_detector(statement)
    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_str


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
