import telebot

bot = telebot.TeleBot("5839756034:AAHBl1NiRzjmmXyjwcAQmb24HLbJblHgJhE")

@bot.message_handler(commands=['start'])
def send_wel(diga):
	bot.reply_to(diga,"foi alterado5")

send_wel(diga,"ok")


bot.infinity_polling()
