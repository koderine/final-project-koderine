from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    #get test to analyse from request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    #store response from function
    response = emotion_detector(text_to_analyze)

    #extract specific values to reference from returned
    anger = response['anger']
    disgust = response['anger']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    #error_handling
    if dominant_emotion is None:
        return '<b>Invalid text! Please try again!</b>'

    return (
        f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}"
        f" and 'sadness': {sadness}. The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    #Run the app on localhost at port 5000.
    app.run(host="0.0.0.0", port=5000)
