import telebot

from ai_engine import *

bot = telebot.TeleBot('7467372440:AAH_4eA_UdxhHcQrkPdgJf1cGIEE1bBuoMI')
#@AI_Chat_Bezna_bot
user_data = {}
WARNING_THRESHOLD = 5  # Точка, после которой выдается предупреждение
MAX_WARNINGS = 3
NEUTRAL_THRESHOLD = 5


# print(NEUTRAL_THRESHOLD)
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, это телеграмм бот AI_Bezna.')


def send_start_message():
    bot.send_message(1394465133, "Я запущен!")

@bot.message_handler()
def main(message):
    global user_data
    user_id = message.from_user.id  # ID пользователя
    bot.send_message(message.chat.id, toxic_pred(str(message.text)))
    # print(message.chat.id, message)
    pred = toxic_pred(str(message.text))
    #bot.send_message(message.chat.id, emotion_pred(str(message.text)))
    if user_id not in user_data:
        user_data[user_id] = {"toxic_count": 0, "warnings": 0, "neutral_count": 0}
    if pred == 'Toxic\n':
        user_data[user_id]["toxic_count"] += 1
        toxic_count = user_data[user_id]["toxic_count"]
        warnings = user_data[user_id]["warnings"]
        # print(user_data[user_id]["toxic_count"], 'toxic')

        # Выдача предупреждений
        if toxic_count >= WARNING_THRESHOLD:
            if warnings < MAX_WARNINGS:
                user_data[user_id]["warnings"] += 1
                user_data[user_id]["toxic_count"] = 0
                bot.send_message(
                    chat_id=message.chat.id,
                    text=f"Пользователь {message.from_user.first_name}, предупреждение {warnings + 1} из {MAX_WARNINGS}."
                )
        if warnings == MAX_WARNINGS:
            bot.send_message(
                chat_id=message.chat.id,
                text=f"Пользователь {message.from_user.first_name} заблокирован за токсичное поведение."
            )
        # print(user_data[user_id]["warnings"], 'Количество предупреждений')
    else:
        if user_data[user_id]["warnings"] > 0:
            # Сообщение не токсично, увеличиваем счетчик нейтральных сообщений
            user_data[user_id]["neutral_count"] += 1
            # print(user_data[user_id]["neutral_count"], 'neutral')
            # Если достигнут порог нейтральных сообщений, сбрасываем токсичность
            if user_data[user_id]["neutral_count"] >= NEUTRAL_THRESHOLD:
                if user_data[user_id]["warnings"] > 0:
                    user_data[user_id]["warnings"] -= 1
                    # print(user_data[user_id]["warnings"])
                    user_data[user_id]["neutral_count"] = 0  # Сбрасываем счетчик нейтральных сообщений
                    bot.send_message(
                        chat_id=message.chat.id,
                        text=f"Пользователь {message.from_user.first_name}, вы реабилитировались. Одно предупреждение сброшено. Теперь у вас {user_data[user_id]["warnings"]} предупреждений."
                    )

                    # bot.ban_chat_member(chat_id=message.chat.id, user_id=user_id)
                    #print(user_data[user_id]["toxic_count"])




    with open('Dorabotka.txt', 'a') as file:
        file.write(str(message.text) + '@' + toxic_pred(str(message.text)) + '\n')

# @bot.message_handler()
# def main(message):
#     bot.send_message(message.chat.id, (emotion.predict(list(message))))


send_start_message()
bot.polling(none_stop=True)