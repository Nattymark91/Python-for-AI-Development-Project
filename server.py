"""Server"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")
@app.route("/")
def render_index_page():
    """render index"""
    return render_template('index.html')
@app.route("/emotionDetector")
def emo_detector():
    """response"""
    response = emotion_detector(request.args.get('textToAnalyze'))
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if None in response.values():
        response = " Invalid text! Please try again!"
    else:
        values = (anger, disgust, fear, joy, sadness, dominant_emotion)
        response = f"For the given statement, the system response is 'anger': {values[0]},\
         'disgust': {values[1]}, 'fear': {values[2]},\
          'joy': {values[3]} and 'sadness': {values[4]}.\
           The dominant emotion is {values[5]}."
    return response
if __name__ == "__main__":
    app.run(host="localhost", port=5000)
 