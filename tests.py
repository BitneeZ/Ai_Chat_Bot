import sys
import numpy as np
import pickle
import re
from Stemmer import Stemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


import pandas as pd

df = pd.read_parquet("D:/Github_bezna/toxicator-ru/data/train-00000-of-00001.parquet")
df = df.drop('instruction', axis=1)
df = df.drop('input', axis=1)
print(df)
df.to_csv('toxicis.csv', encoding='utf-8', index=False)
# emotion_columns = df.filter(like="эмоция").columns
# df = df.drop('text', axis=1)
# df = df.drop('id', axis=1)
# df = df.drop('author', axis=1)
# df = df.drop('subreddit', axis=1)
# df = df.drop('link_id', axis=1)
# df = df.drop('parent_id', axis=1)
# df = df.drop('created_utc', axis=1)
# df = df.drop('rater_id', axis=1)
# df = df.drop('example_very_unclear', axis=1)
#
# print(df.columns)
#
# emotion_columns = ['admiration', 'amusement', 'anger', 'annoyance', 'approval',
#        'caring', 'confusion', 'curiosity', 'desire', 'disappointment',
#        'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear',
#        'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride',
#        'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
#
# # Создадим новый столбец с эмоцией
# df['emotions'] = df[emotion_columns].idxmax(axis=1)
#
# for i in ['admiration', 'amusement', 'anger', 'annoyance', 'approval',
#        'caring', 'confusion', 'curiosity', 'desire', 'disappointment',
#        'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear',
#        'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride',
#        'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']:
#     df = df.drop(i, axis=1)
#
# # Результат
# print(df)
#
# df.to_csv('emotions.csv', encoding='utf-8', index=False)