import telebot
from telebot import types

bot = telebot.TeleBot('BotApi')


@bot.message_handler(commands=['start'])
def start(message, x=0):
    for i in open('chatids.txt', 'r').readlines():
        if i == str(message.chat.id) + '\n':
            x = 1
            break
    if x == 0:
        with open('chatids.txt', 'a+') as chatids:
            print(message.chat.id, file=chatids)
            bot.send_message(message.chat.id, 'Вы добавлены в базу.')
    else:
        bot.send_message(message.chat.id, 'Вы уже в базе.')


@bot.message_handler(commands=['rassylka'])
def rassylka(message):
    if message.chat.id == 127154290:
        for i in open('chatids.txt', 'r').readlines():
            bot.send_message(i, 'рассылка')
    else:
        bot.send_message(message.chat.id, 'недостаточно прав')


bot.polling()
