import telebot

bot = telebot.TeleBot("5839756034:AAHBl1NiRzjmmXyjwcAQmb24HLbJblHgJhE")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(diga):
	bot.reply_to(diga, "foi alterado")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
