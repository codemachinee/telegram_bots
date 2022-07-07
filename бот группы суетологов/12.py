import telebot
import os
from telebot import types
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from random import *

token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token)

kb1 = types.InlineKeyboardMarkup(row_width=1)
but1 = types.InlineKeyboardButton(text='Купить билет в Орёл',
                                  url='https://жд-билеты.сайт/kupit-zhd-bilety/#/moskva/orel?')
but2 = types.InlineKeyboardButton(text='Бронь стола на Привале', url='http://onmap.uz/tel/74862484006')
but3 = types.InlineKeyboardButton(text='Бронь стола 7 пятниц', url='http://onmap.uz/tel/74862490008')
but4 = types.InlineKeyboardButton(text='Бронь стола Шаривари', url='http://onmap.uz/tel/74862445303')
but5 = types.InlineKeyboardButton(text='Важное про Орёл', callback_data='btn')
kb1.add(but1, but2, but3, but4, but5)


def pidr():
    x = choice([1, 2, 3, 4, 5, 6, 7])
    if x == 1:
        file1 = open("Я.png", 'rb')
        y = ("Игорь", file1)
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!!! Пидарасом дня 
        {datetime.now().year, datetime.now().month, datetime.now().day} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')
    if x == 2:
        file1 = open("Филч.png", 'rb')
        y = ("Филч", file1)
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!!! Пидарасом дня 
        {datetime.now().year, datetime.now().month, datetime.now().day} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')
    if x == 3:
        file1 = open("Серега.png", 'rb')
        y = ("Серега", file1)
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!! Пидарасом дня 
        {datetime.now().year, datetime.now().month, datetime.now().day} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')
    if x == 4:
        file1 = open("Леха.png", 'rb')
        y = ("Леха(Саня)", file1)
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!! Пидарасом дня 
        {datetime.now().year, datetime.now().month, datetime.now().day} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')
    if x == 5:
        file1 = open("фитиль.jpg", 'rb')
        y = ("Леха(Фитиль)", file1)
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!! Пидарасом дня 
        {datetime.now().year, datetime.now().month, datetime.now().day} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')
    if x == 6:
        file1 = open("маугли.png", 'rb')
        y = ("Маугли", file1)
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!! Пидарасом дня 
        {datetime.now().year, datetime.now().month, datetime.now().day} объявляется {y[0]} 


                                                                            Вызвать орловского помощника: /orel''')
    if x == 7:
        file1 = open("саня.png", 'rb')
        y = ("Саня", file1)
        bot.send_photo('@hloappstest', y[1])
        bot.send_message('@hloappstest', f'''Всем привет!! Пидарасом дня 
        {datetime.now().year, datetime.now().month, datetime.now().day} объявляется {y[0]} 


                                                                                    Вызвать орловского помощника: /orel''')


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    if callback.data == 'btn':
        file2 = open("важно.png", 'rb')
        bot.send_photo('@hloappstest', file2)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(pidr, 'cron', day_of_week='mon-sun', hour=11)
    scheduler.start()

    try:
        @bot.message_handler(commands=['orel'])
        def orel(message):
            bot.send_message('@hloappstest', 'Орловский помощник..', reply_markup=kb1)
    except KeyboardInterrupt:
        pass


bot.polling()
