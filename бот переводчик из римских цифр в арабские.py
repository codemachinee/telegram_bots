import telebot
from my_function import translate

bot = telebot.TeleBot('BotApi')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'''Вас приветствует переводчик из римских цифр в арабские.

Уважаемый {message.from_user.first_name}, введите римскую цифру:''')

    @bot.message_handler(regexp=r"[IXVCDLM]")
    def answer(message):
        bot.send_message(message.chat.id, f''''Ответ: {translate(message)}''')


bot.polling()
