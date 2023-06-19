import telebot

bot = telebot.TeleBot("5839756034:AAHBl1NiRzjmmXyjwcAQmb24HLbJblHgJhE")

@bot.message_handler(commands=['start'])
def messag(dizer):
	bot.reply_to(dizer,'foi alterado1')


@bot.message_handler(content_types=['document', 'audio'])
if content_types == 'audio':
	def handle_docs_audio(message):
		bot.reply_to(message, 'ok')

bot.infinity_polling()
