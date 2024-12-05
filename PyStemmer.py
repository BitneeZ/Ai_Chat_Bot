import sys
import numpy as np
import pickle
import re
from Stemmer import Stemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# очистка текста с помощью regexp приведение слов в инфинитив и нижний регистр, замена цифр

def text_cleaner(text):
    text = text.lower()  # приведение в lowercase
    stemmer = Stemmer('russian')
    text = ' '.join(stemmer.stemWords(text.split()))
    text = re.sub(r'\b\d+\b', ' digit ', text)  # замена цифр
    return text


# загрузка данных из файла model.txt

def load_data():
    data = {'text': [], 'tag': []}
    #for line in open('D:/Github_bezna/Ai_Chat_Bot/test.txt', encoding='utf-8'):
    for line in open('D:/Github_bezna/Ai_Chat_Bot/AI_GEN.txt', encoding='utf-8'):
        if not ('#' in line):
            row = line.split("@")
            data['text'] += [row[0]]
            #print([row[1]])
            data['tag'] += [row[1]]
            #print(len(data['tag']))


    return data


# Обучение

def train_test_split(data, validation_split=0.1):
    sz = len(data['text'])
    indices = np.arange(sz)
    np.random.shuffle(indices)

    X = [data['text'][i] for i in indices]
    Y = [data['tag'][i] for i in indices]
    nb_validation_samples = int(validation_split * sz)

    return {
        'train': {'x': X[:-nb_validation_samples], 'y': Y[:-nb_validation_samples]},
        'test': {'x': X[-nb_validation_samples:], 'y': Y[-nb_validation_samples:]}
    }



# - - - -

def openai(xd):
    data = load_data()
    D = train_test_split(data)
    text_clf = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', SGDClassifier(loss='hinge')),
    ])
    text_clf.fit(D['train']['x'], D['train']['y'])
    predicted = text_clf.predict(D['train']['x'])

    # Начало тестирования программы


    z = xd
    zz = []
    zz.append(z)
    predicted = text_clf.predict(zz)
    res = predicted[0]
    return res

