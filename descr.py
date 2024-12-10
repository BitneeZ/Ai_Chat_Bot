import pandas as pd
import sys
import numpy as np
import pickle
import re
# df = pd.read_csv('labeled.csv')
# print(df)
# file = open('Panama.txt', 'w')
# for index, row in df.iterrows():
#     # print(row, end="")
#     if row['toxic'] == 1.0:
#         print('@Toxic ' + row['comment'], end="")
#         file.write('@Toxic ' + row['comment'])
#     else:
#         print('@Neutral ' + row['comment'], end="")
#         file.write('@Neutral ' + row['comment'])

# df['toxic'] = df['toxic'].replace(1.0, "@Toxic")
# df['toxic'] = df['toxic'].replace(0.0, "@Neutral")
# print(df)
# df['toxic'] = df['toxic'] + "@Toxic"
#
# print(df)

# df.to_csv('toxic4.csv', encoding='utf-8', index=False)

# def load_data():
#     data = {'text':[],'tag':[]}
#     for line in open('Panama.txt'):
#         if not('#' in line):
#             row = line.split("@")
#             row = [row[1], row[0]]
#             data['tag'] += [row[0]]
#             data['text'] += [row[1]]
#             with open('Panama2.txt', 'a') as file:
#                 file.write(str(row) + '\n')
#
#
#
# load_data()










