"""
This module analyzes emotion detection results from IBM's Emotion Detection API.

It parses the API response, extracts emotion scores, and identifies the dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection. emotion_detection import emotion_detection

app = Flask("Emotion detector")

@app. route("/emotionDetector")

def sent_analyzer():
    """
    Retrieve the text to analyze from the request arguments
    
    """

    text_to_analyze = request.args.get ('textToAnalyze')
# Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detection (text_to_analyze)
# Extract the label and score from the response
# Return a formatted string with the sentiment label and score

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return "For the given statement, the system response is 'anger':"+\
        f"{response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']},"+\
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}."+\
        f"The dominant emotion is {response['dominant_emotion']}."

@app. route ("/")
def render_index_page():
    """
    load the index page

    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
