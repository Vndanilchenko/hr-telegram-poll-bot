"""
бот опроса соискателей о причинах отказа от позиции

@ author: vndanilchenko@gmail.com
"""



import telebot, os

# импортируем токены
try:
    token = os.environ['TG_TOKEN']
except:
    from private.token import token

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Лена')

bot.polling()