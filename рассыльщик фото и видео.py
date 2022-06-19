 import telebot

bot = telebot.TeleBot('Bot Api')


@bot.message_handler(commands=['start'])
def start(message):
    file1 = open('для автоаллюр.png', 'rb')
    file2 = open('Новый проект.mp4', 'rb')
    bot.send_photo(message.chat.id, file1, "норм фото")
    bot.send_video(message.chat.id, file2,)
    bot.send_photo(message.chat.id, "https://www.wikitechy.com/tutorials/python/img/python-images/python-regex.png",
                   "норм фото с инета")
    bot.send_video(message.chat.id,
                   'https://www.youtube.com/watch?v=2SsC4WH0hys&list=PLmSBSL0-aSglhQu_apL_4GM8VbUKuL2J_&index=7')


bot.polling()
