from joblib import load
toxic = load('toxic.joblib')
emotion = load('emotions_AI.joblib')
message = ["Ты молодец"]
print(toxic.predict(message))
