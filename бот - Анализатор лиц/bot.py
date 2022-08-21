import telebot
from telebot import types
import os

from face_oko import face_verify, face_analyze

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """Приветствую! Мое предназначение сравнивать и анализировать фото.
Выбери необходимую опцию.""")
    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    but1 = types.KeyboardButton(text='Проверить человека с фото на принадлежность к суетологам')
    but2 = types.KeyboardButton(text='Узнать пол, возраст, расу и эмоции по фото')
    kb1.add(but1, but2)
    bot.send_message(message.chat.id, '...', reply_markup=kb1)


@bot.message_handler(func=lambda x: x.text)
def chek_message(x):
    if x.text == 'Проверить человека с фото на принадлежность к суетологам':
        kb2 = types.ReplyKeyboardRemove()
        bot.send_message(x.chat.id, '...', reply_markup=kb2)
        sent = bot.send_message(x.chat.id, 'Отправь фото на проверку..')
        bot.register_next_step_handler(sent, verify)

    if x.text == 'Узнать пол, возраст, расу и эмоции по фото':
        kb2 = types.ReplyKeyboardRemove()
        bot.send_message(x.chat.id, '...', reply_markup=kb2)
        sent = bot.send_message(x.chat.id, 'Отправь фото на проверку..')
        bot.register_next_step_handler(sent, analyze)


def verify(message):
    bot.send_message(message.chat.id, 'терпение..это займет пару минут..')
    message_to_save = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(message_to_save.file_path)
    src = f'лица/' + message_to_save.file_path
    with open(src, 'wb') as image_file:
        image_file.write(downloaded_file)
        bot.send_message(message.chat.id, face_verify(img_1=src))
        os.remove(src)
        kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        but1 = types.KeyboardButton(text='Проверить человека с фото на принадлежность к суетологам')
        but2 = types.KeyboardButton(text='Узнать пол, возраст, расу и эмоции по фото')
        kb1.add(but1, but2)
        bot.send_message(message.chat.id, '...', reply_markup=kb1)


def analyze(message):
    bot.send_message(message.chat.id, 'терпение..это займет пару минут..')
    message_to_save = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(message_to_save.file_path)
    src = f'лица/' + message_to_save.file_path
    with open(src, 'wb') as image_file:
        image_file.write(downloaded_file)
        bot.send_message(message.chat.id, face_analyze(img_1=src))
        os.remove(src)
        kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        but1 = types.KeyboardButton(text='Проверить человека с фото на принадлежность к суетологам')
        but2 = types.KeyboardButton(text='Узнать пол, возраст, расу и эмоции по фото')
        kb1.add(but1, but2)
        bot.send_message(message.chat.id, '...', reply_markup=kb1)


bot.polling()
