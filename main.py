import telebot
from api import *
token = '6385241128:AAHOw7TCbd1IcMhiERFHwNpvmfEFOUAZKjQ'

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def welcome(message):
  bot.send_message(message.chat.id, '👋Salom Telegram botimizga xush kelibsiz\n🤖 Bu botda Siz Ob havoni bilishiz mumkin\n💼 Botni ishlatish osson Shahar nomini kiriting')


@bot.message_handler(func=lambda message: True)
def msg(message):
  try:
    shahar = message.text
    data = obhavo(shahar)
    if data == "Error":
      bot.send_message(message.chat.id, 'Bunday shahar topilmadi')
    else:
      bot.send_message(message.chat.id, data)
  except:
    bot.send_message(message.chat.id, "Xato!!!")

if __name__ == "__main__":
  bot.polling(none_stop=True)
