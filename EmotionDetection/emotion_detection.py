import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputjson = { "raw_document": { "text": text_to_analyse } }
    
    resp = requests.post(url, json = inputjson, headers=header)
    response = json.loads(resp.text)

    if resp.status_code == 400:
       response =     {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                    }

    else:

        emotions = response['emotionPredictions'][0]['emotionMentions'][0]['emotion']

        response =  {
                'anger': response['emotionPredictions'][0]['emotion']['anger'],
                'disgust': response['emotionPredictions'][0]['emotion']['disgust'],
                'fear': response['emotionPredictions'][0]['emotion']['fear'],
                'joy': response['emotionPredictions'][0]['emotion']['joy'],
                'sadness': response['emotionPredictions'][0]['emotion']['sadness'],
                'dominant_emotion': max(emotions, key=emotions.get)
                    }

    return response