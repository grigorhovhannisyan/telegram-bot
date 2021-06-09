import telebot

bot = telebot.TeleBot('1877524228:AAHAtgaxzT5Ul915mMSU8h1xDAUxCV_mELI')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

    @bot.message_handler(content_types=['text']) 

    def get_text_messages(message):
       if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
       else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

        bot.polling(none_stop=False)
print("hello")
