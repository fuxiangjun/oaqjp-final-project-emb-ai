import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detection(text_to_analyse):  # Define a function  that takes a string input (text_to_analyse)
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"  # URL of the emotion analysis service
    
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    if response.status_code == 200 :

        response_dict=response.json()

        emotions=response_dict['emotionPredictions'][0]['emotion']

        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)
    elif response.status_code == 400 :
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None

        
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    
    if response.status_code == 400:
        dominant_emotion = None
    else :
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    result = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }

    return result 