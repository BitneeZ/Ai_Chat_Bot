from joblib import load
toxic = load('toxic.joblib')
emotion = load('emotions_AI.joblib')
def toxic_pred(msg):
    res = toxic.predict(list(msg))
    return res

def emotion_pred(msg):
    res = emotion.predict(list(msg))
    return res