from joblib import load
toxic = load('toxic_v4.joblib')
emotion = load('emotions_AI.joblib')


def toxic_pred(msg):
    z = msg
    zz = []
    zz.append(z)
    predicted = toxic.predict(zz)
    res = predicted[0]
    return res

def emotion_pred(msg):
    z = msg
    zz = []
    zz.append(z)
    predicted = emotion.predict(zz)
    res = predicted[0]
    return res
