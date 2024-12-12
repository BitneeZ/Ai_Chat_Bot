from joblib import load

toxic = load('AI/toxic_v10.joblib')
emotion = load('AI/emotions_AI.joblib')


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
