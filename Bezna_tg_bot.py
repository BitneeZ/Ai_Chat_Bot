import telebot

bot = telebot.TeleBot('7467372440:AAH_4eA_UdxhHcQrkPdgJf1cGIEE1bBuoMI')
from joblib import load
toxic = load('sgd_model.joblib')
emotion = load('emotions_AI.joblib')
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, это телеграмм бот AI_Bezna.')

@bot.message_handler()
def main(message):
    bot.send_message(message.chat.id, (toxic.predict(message)))

# @bot.message_handler()
# def main(message):
#     bot.send_message(message.chat.id, (emotion.predict(list(message))))

bot.polling(none_stop=True)