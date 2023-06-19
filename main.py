import telebot

bot = telebot.TeleBot("5839756034:AAHBl1NiRzjmmXyjwcAQmb24HLbJblHgJhE")

@bot.message_handler(commands=['start'])
def send_wel(diga):
	bot.reply_to("foi alterado4")


bot.infinity_polling()
