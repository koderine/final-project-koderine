from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    #get text to analyse from request arguments
    text_to_analyse = request.args.get('textToAnalyse')

    #store response from function in variable
    response = emotion_detector(text_to_analyse)

    #extract specific values to reference in return
    anger = response['anger']
    disgust = reponse['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dom_emotion = response['dominant_emotion']

    if response[dom_emotion] is None:
        return 'Invalid text! Please try again!'
    
    return (f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. The dominant emotion is {dom_emotion}")

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000)
