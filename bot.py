import bot


bot = telebot.TeleBot("6261638502:AAGMQRbxtslGCvtqCZwj8HnOF5t-cZXn-FQ")

@bot.message_handler(commands=['Старт'])
def main(message):
    bot.send_massage(message.chat.id, 'Hello')
bot.infinity_polling()