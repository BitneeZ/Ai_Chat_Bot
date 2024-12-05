import telebot
from PyStemmer import *

bot = telebot.TeleBot('7467372440:AAH_4eA_UdxhHcQrkPdgJf1cGIEE1bBuoMI')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, это телеграмм бот AI_Bezna.')

@bot.message_handler()
def main(message):
    bot.send_message(message.chat.id, openai(str(message)))

### Xd

bot.polling(none_stop=True)