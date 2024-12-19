import json

# Чтение файла JSON
with open('Chat_-1002371061776_members.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data["1394465133"]["toxic_count"])

with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
    user_data = json.load(file)
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)  # Загружаем данные из файла
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
        with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
            user_data = json.load(file)

            json.dump(user_data, file, indent=4, ensure_ascii=False)
        with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
            user_data = json.load(file)

        with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
            json.dump(user_data, file, indent=4, ensure_ascii=False)
        with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
            user_data = json.load(file)

        user_data.append(user_data[user_id])
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4,
              ensure_ascii=False)  # indent=4 для читабельности, ensure_ascii=False для сохранения кириллицы
    print("Файл data.json успешно создан!")
