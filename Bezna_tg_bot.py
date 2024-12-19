import json
from random import randint as rn

import telebot

from ai_engine import *

bot = telebot.TeleBot('7467372440:AAH_4eA_UdxhHcQrkPdgJf1cGIEE1bBuoMI')
#@AI_Chat_Bezna_bot
user_datas = {}
user_data = {}
WARNING_THRESHOLD_0 = rn(7, 15)  # Точка, после которой выдается предупреждение
WARNING_THRESHOLD_1 = rn(3, 7)
WARNING_THRESHOLD_2 = rn(1, 3)
print(WARNING_THRESHOLD_0, WARNING_THRESHOLD_1, WARNING_THRESHOLD_2)
MAX_WARNINGS = 3
NEUTRAL_THRESHOLD_0 = rn(45, 130)
NEUTRAL_THRESHOLD_1 = rn(130, 245)
NEUTRAL_THRESHOLD_2 = rn(245, 350)
print(NEUTRAL_THRESHOLD_0, NEUTRAL_THRESHOLD_1, NEUTRAL_THRESHOLD_2)

# print(NEUTRAL_THRESHOLD)
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, это телеграмм бот AI_Bezna.')


def send_start_message():
    bot.send_message(1394465133, "Я запущен!")


@bot.message_handler()
def main(message):
    global user_datas
    user_id = message.from_user.id  # ID пользователя
    bot.send_message(message.chat.id, toxic_pred(str(message.text)))
    # print(message.chat.id, message)
    pred = toxic_pred(str(message.text))
    #bot.send_message(message.chat.id, emotion_pred(str(message.text)))
    user_datas = {}
    try:
        with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
            user_datas = json.load(file)
    except:
        with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
            json.dump(user_datas, file, indent=4,
                      ensure_ascii=False)  # indent=4 для читабельности, ensure_ascii=False для сохранения кириллицы

    with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
        user_datas = json.load(file)
        # print(user_datas)
    if str(user_id) not in user_datas:
        user_data[user_id] = {"toxic_count": 0, "warnings": 0, "neutral_count": 0}
        # print(user_data)
        user_datas.update(user_data)
        # print(user_datas)
        with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
            json.dump(user_datas, file, indent=4, ensure_ascii=False)  # Сохраняем в формате JSON
            # print("Данные успешно добавлены в JSON-файл!")
        # user_data[user_id].append(user_data)
        # json.dump(user_data, file, indent=4,
        #           ensure_ascii=False)
    if pred == 'Toxic\n':
        with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
            user_datas = json.load(file)
        if user_datas[str(user_id)]["warnings"] < MAX_WARNINGS:
            user_datas[str(user_id)]["toxic_count"] += 1
        toxic_count = user_datas[str(user_id)]["toxic_count"]
        warnings = user_datas[str(user_id)]["warnings"]
        # print(user_data[user_id]["toxic_count"], 'toxic')
        user_datas.update(user_datas)
        with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
            json.dump(user_datas, file, indent=4, ensure_ascii=False)  # Сохраняем в формате JSON
        # Выдача предупреждений
        with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
            user_datas = json.load(file)
        if user_datas[str(user_id)]["warnings"] == 0:
            if user_datas[str(user_id)]["toxic_count"] >= WARNING_THRESHOLD_0:
                if user_datas[str(user_id)]["warnings"] < MAX_WARNINGS:
                    user_datas[str(user_id)]["warnings"] += 1
                    user_datas[str(user_id)]["toxic_count"] = 0
                    user_datas.update(user_datas)
                    with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
                        json.dump(user_datas, file, indent=4, ensure_ascii=False)  # Сохраняем в формате JSON

                    bot.send_message(
                        chat_id=message.chat.id,
                        text=f"Пользователь {message.from_user.first_name}, предупреждение {warnings + 1} из {MAX_WARNINGS}. \n"
                             f"Если продолжите, следующие предупреждения будут даваться намного быстрее."
                    )
        elif user_datas[str(user_id)]["warnings"] == 1:
            with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
                user_datas = json.load(file)
            if user_datas[str(user_id)]["toxic_count"] >= WARNING_THRESHOLD_1:
                if user_datas[str(user_id)]["warnings"] < MAX_WARNINGS:
                    user_datas[str(user_id)]["warnings"] += 1
                    user_datas[str(user_id)]["toxic_count"] = 0
                    user_datas.update(user_datas)
                    with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
                        json.dump(user_datas, file, indent=4, ensure_ascii=False)  # Сохраняем в формате JSON

                    bot.send_message(
                        chat_id=message.chat.id,
                        text=f"Пользователь {message.from_user.first_name}, предупреждение {warnings + 1} из {MAX_WARNINGS}."
                    )

        elif user_datas[str(user_id)]["warnings"] == 2:
            with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
                user_datas = json.load(file)
            if user_datas[str(user_id)]["toxic_count"] >= WARNING_THRESHOLD_2:
                if user_datas[str(user_id)]["warnings"] < MAX_WARNINGS:
                    user_datas[str(user_id)]["warnings"] += 1
                    user_datas[str(user_id)]["toxic_count"] = 0
                    user_datas.update(user_datas)
                    with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
                        json.dump(user_datas, file, indent=4, ensure_ascii=False)  # Сохраняем в формате JSON

                    bot.send_message(
                        chat_id=message.chat.id,
                        text=f"Пользователь {message.from_user.first_name}, предупреждение {warnings + 1} из {MAX_WARNINGS}."
                    )


        if user_datas[str(user_id)]["warnings"] == MAX_WARNINGS:
            bot.send_message(
                chat_id=message.chat.id,
                text=f"Пользователь {message.from_user.first_name} заблокирован за токсичное поведение."
            )
            # bot.ban_chat_member(chat_id=message.chat.id, user_id=user_id)

    else:
        with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
            user_datas = json.load(file)
        if user_datas[str(user_id)]["warnings"] > 0:
            # Сообщение не токсично, увеличиваем счетчик нейтральных сообщений
            user_datas[str(user_id)]["neutral_count"] += 1
            with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
                json.dump(user_datas, file, indent=4, ensure_ascii=False)  # Сохраняем в формате JSON
            # print(user_data[user_id]["neutral_count"], 'neutral')
            # Если достигнут порог нейтральных сообщений, сбрасываем токсичность
            with open(f'Chat_{message.chat.id}_members.json', "r", encoding="utf-8") as file:
                user_datas = json.load(file)
            if user_datas[str(user_id)]["warnings"] == 1:
                if user_datas[str(user_id)]["neutral_count"] >= NEUTRAL_THRESHOLD_0:
                    if user_datas[str(user_id)]["warnings"] > 0:
                        user_datas[str(user_id)]["warnings"] -= 1
                        # print(user_data[user_id]["warnings"])
                        user_datas[str(user_id)]["neutral_count"] = 0  # Сбрасываем счетчик нейтральных сообщений
                        with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
                            json.dump(user_datas, file, indent=4, ensure_ascii=False)  # Сохраняем в формате JSON
                        bot.send_message(
                            chat_id=message.chat.id,
                            text=f"Пользователь {message.from_user.first_name}, вы реабилитировались. Одно предупреждение сброшено. Теперь у вас {user_datas[str(user_id)]["warnings"]} предупреждений."
                        )
            elif user_datas[str(user_id)]["warnings"] == 2:
                if user_datas[str(user_id)]["neutral_count"] >= NEUTRAL_THRESHOLD_1:
                    if user_datas[str(user_id)]["warnings"] > 0:
                        user_datas[str(user_id)]["warnings"] -= 1
                        # print(user_data[user_id]["warnings"])
                        user_datas[str(user_id)]["neutral_count"] = 0  # Сбрасываем счетчик нейтральных сообщений
                        with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
                            json.dump(user_datas, file, indent=4, ensure_ascii=False)  # Сохраняем в формате JSON
                        bot.send_message(
                            chat_id=message.chat.id,
                            text=f"Пользователь {message.from_user.first_name}, вы реабилитировались. Одно предупреждение сброшено. Теперь у вас {user_datas[str(user_id)]["warnings"]} предупреждений."
                        )
            elif user_datas[str(user_id)]["warnings"] == 3:
                if user_datas[str(user_id)]["neutral_count"] >= NEUTRAL_THRESHOLD_2:
                    if user_datas[str(user_id)]["warnings"] > 0:
                        user_datas[str(user_id)]["warnings"] -= 1
                        # print(user_data[user_id]["warnings"])
                        user_datas[str(user_id)]["neutral_count"] = 0  # Сбрасываем счетчик нейтральных сообщений
                        with open(f'Chat_{message.chat.id}_members.json', "w", encoding="utf-8") as file:
                            json.dump(user_datas, file, indent=4, ensure_ascii=False)  # Сохраняем в формате JSON
                        bot.send_message(
                            chat_id=message.chat.id,
                            text=f"Пользователь {message.from_user.first_name}, вы реабилитировались. Одно предупреждение сброшено. Теперь у вас {user_datas[str(user_id)]["warnings"]} предупреждений."
                        )

    with open('Dorabotka.txt', 'a') as file:
        file.write(str(message.text) + '@' + toxic_pred(str(message.text)) + '\n')

# @bot.message_handler()
# def main(message):
#     bot.send_message(message.chat.id, (emotion.predict(list(message))))


send_start_message()
bot.polling(none_stop=True)