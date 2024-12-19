import json

# Чтение файла JSON
with open('Chat_-1002371061776_members.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data["1394465133"]["toxic_count"])
