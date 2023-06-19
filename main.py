import telebot

bot = telebot.TeleBot("5839756034:AAHBl1NiRzjmmXyjwcAQmb24HLbJblHgJhE")


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	pass

bot.infinity_polling()
