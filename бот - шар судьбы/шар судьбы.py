import telebot
from telebot import types
from random import *

token =
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def check_start(message):
    start_file = open("ball/start_image.png", 'rb')
    bot.send_photo(message.chat.id, start_file)
    bot.send_message(message.chat.id, '''Решил попытать удачу или просто переложить ответственность?
Что ж.. Чтобы все прошло как надо просто переведи сотку моему создателю на сбер и погладь шар''')
    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    but1 = types.KeyboardButton(text='Погладить шар')
    but2 = types.KeyboardButton(text='Шар отбой')
    kb1.add(but1, but2)
    bot.send_message(message.chat.id, '...', reply_markup=kb1)


def ball_of_fate():
    ball_choice = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    if ball_choice == 1:
        ball_answer = open("ball/var_one.png", 'rb')
        return ball_answer
    if ball_choice == 2:
        ball_answer = open("ball/var_two.png", 'rb')
        return ball_answer
    if ball_choice == 3:
        ball_answer = open("ball/var_tree.png", 'rb')
        return ball_answer
    if ball_choice == 4:
        ball_answer = open("ball/var_four.png", 'rb')
        return ball_answer
    if ball_choice == 5:
        ball_answer = open("ball/var_five.png", 'rb')
        return ball_answer
    if ball_choice == 6:
        ball_answer = open("ball/var_six.png", 'rb')
        return ball_answer
    if ball_choice == 7:
        ball_answer = open("ball/var_seven.png", 'rb')
        return ball_answer
    if ball_choice == 8:
        ball_answer = open("ball/var_eight.png", 'rb')
        return ball_answer
    if ball_choice == 9:
        ball_answer = open("ball/var_nine.png", 'rb')
        return ball_answer
    if ball_choice == 10:
        ball_answer = open("ball/var_ten.png", 'rb')
        return ball_answer
    if ball_choice == 11:
        ball_answer = open("ball/var_eleven.png", 'rb')
        return ball_answer


@bot.message_handler(func=lambda v: v.text)
def chek_message(v):
    if v.text == 'Погладить шар':
        bot.send_photo(v.chat.id, ball_of_fate())
    if v.text == 'Шар отбой':
        kb2 = types.ReplyKeyboardRemove()
        bot.send_message(v.chat.id, '...', reply_markup=kb2)


bot.polling()
