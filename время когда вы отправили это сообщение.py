import telebot
import datetime

bot = telebot.TeleBot('BotApi')

@bot.message_handler(commands=['start'])
def start(message):
    date = datetime.datetime.utcfromtimestamp(message.date + 10800)   # 10800 - в переводе с секунд=+3часа -
    # московская часовая зона
    bot.send_message(message.chat.id, f'''Время, когда Вы отправили это сообщение: {date}''')


bot.polling()