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
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[1]) + 1)
            s0.pop(1)
            s0.insert(1, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 2:
        file1 = open("Филч.png", 'rb')
        y = ("Филч", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[0]) + 1)
            s0.pop(0)
            s0.insert(0, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 3:
        file1 = open("Серега.png", 'rb')
        y = ("Серега", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[2]) + 1)
            s0.pop(2)
            s0.insert(2, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 4:
        file1 = open("Леха.png", 'rb')
        y = ("Леха(Саня)", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[4]) + 1)
            s0.pop(4)
            s0.insert(4, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 5:
        file1 = open("фитиль.jpg", 'rb')
        y = ("Леха(Фитиль)", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[5]) + 1)
            s0.pop(5)
            s0.insert(5, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 6:
        file1 = open("маугли.png", 'rb')
        y = ("Маугли", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[6]) + 1)
            s0.pop(6)
            s0.insert(6, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 7:
        file1 = open("саня.png", 'rb')
        y = ("Саня", file1)
        with open("статистика", 'r+') as stat_file:
            s0 = stat_file.read().split(sep='\n')
            s1 = str(int(s0[3]) + 1)
            s0.pop(3)
            s0.insert(3, s1)
            s2 = '\n'.join(s0)
        with open("статистика", 'w') as stat_file:
            stat_file.write(str(s2))
        bot.send_photo('@suetologyorla', y[1])
        bot.send_message('@suetologyorla', f'''Всем привет!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()
        
        
def dr():
    if datetime.now().day == 20 and datetime.now().month == 4:
        bot.send_message('@suetologyorla', (f' Дорогие друзья! Все эти рейтинги и звания конечно очень круто, но это '
                                          f'ежедневная рутина. Сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник '
                                          f'всего этого Игорь, да именно он вне всяких рейтингов и чартов, ведь у него '
                                          f'самый большой член в этом сообществе и самый скромный нрав. Игорян с днем '
                                          f'рождения!!! Двигайся по поводу и без, главное не останавливайся!'))
        bot.send_message('@suetologyorla', 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 27 and datetime.now().month == 4:
        bot.send_message('@suetologyorla', (f' Дорогие друзья! Все эти рейтинги и звания конечно очень круто, но это '
                                          f'ежедневная рутина. Сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник '
                                          f'всего этого Алексей! И вы спросите: "тот Алексей который Саня?" - и я вам '
                                          f'отвечу: нет! Этот парень настолько легендарный, что его видно издалека. '
                                          f'Многие девушки/женщины могут делать ему миньет не вставая на колени, но они'
                                          f' его давно не интересуют.. В трудное время он мог бы быть солнечными '
                                          f'часами или глубиномером, но а пока он решил побыть глиномесом)). Леха с '
                                          f'днем рождения!!! Расти, качественно хавай и продолжай бежать так, как никто'
                                          f' никогда не бежал!'))
        bot.send_message('@suetologyorla', 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 5 and datetime.now().month == 5:
        bot.send_message('@suetologyorla', f''' Дорогие друзья! Все эти рейтинги и звания конечно очень круто, но это
ежедневная рутина. Сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник всего этого Илюха, он же легендарный Филч!
Обладатель фамилии на которую были забронированы все столики заведений Орла, а также способности вызывать 
умиление у самых непробиваемых девушек как молодого зала, так и женщин зала милф...жаль ему эта способность не нужна ибо
он на другой стороне. Илюха с днем рождения!!! Выскакивай на челноке, но только не на Герценском мосту!''')
        bot.send_message('@suetologyorla', 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 14 and datetime.now().month == 7:
        bot.send_message('@suetologyorla', (f' Дорогие друзья! Все эти рейтинги и звания конечно очень круто,но это'
                                          f'ежедневная рутина. Сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник '
                                          f'всего этого Диман, он же Маугли. Скрытый обитатель каменных джунглей, '
                                          f'который отрабатывает свои тактики подкатывания через третих лиц прикрываясь'
                                          f'женатостью, но мы то все прекрасно знаем какие цели он приследует на самом '
                                          f'деле)) Знает толк в кальянах и кальянщиках. Диман с днем рождения!!! '
                                          f'Достигай всех своих целей!'))
        bot.send_message('@suetologyorla', 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 16 and datetime.now().month == 7:
        bot.send_message('@suetologyorla', (f' Дорогие друзья! Все эти рейтинги и звания конечно очень круто, но это '
                                          f'ежедневная рутина. Сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник '
                                          f'всего этого СерГей, да именно он вне всяких рейтингов и чартов, ведь даже в'
                                          f' его имени есть частица того, что согревало по ночам Фредди Меркьюри, Нила '
                                          f'Патрика Харриса и конечно же Бориса Моисеева. Серега с днем рождения!!! '
                                          f'Кайфуй, твори, созидай! Будь ласков как Басков.'))
        bot.send_message('@suetologyorla', 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 8 and datetime.now().month == 9:
        bot.send_message('@suetologyorla', f''' Дорогие друзья! Все эти рейтинги и звания конечно очень круто, но это 
ежедневная рутина. Сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник всего этого Саня! Тот самый младший обитатель 
нашего сообщества, который мог бы качественно использовать опыт старших товарищей, но использовать особо нечего. Чтобы 
Саня себе не напланировал все закончится построением перетекающим в сон с мужиками. 
Саня с днем рождения!!! Кайфуй, не теряй время и скорее заканчивай шарагу!''')
        bot.send_message('@suetologyorla', 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 17 and datetime.now().month == 11:
        bot.send_message('@suetologyorla', (f' Дорогие друзья! Все эти рейтинги и звания конечно очень круто, но это '
                                          f'ежедневная рутина. Сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник '
                                          f'всего этого Леха! Вы спросите: "тот самый длинный Леха?" - и я отвечу: нет!'
                                          f' Тот Леха, который Саня. И Скажу еще то, что длину своего роста и заодно '
                                          f'члена он компенсирует длиной тайма в ФИФЕ. Легендарный сомелье всего что '
                                          f'горит и просто пиздатый пацан. Леха с днем рождения!!! Пусть ФИФА длится '
                                          f'столько сколько тебе нужно брат!'))
        bot.send_message('@suetologyorla', 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    if callback.data == 'btn':
        file2 = open("важно.png", 'rb')
        bot.send_photo('@suetologyorla', file2)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message('@suetologyorla', ('Основные команды поддерживаемые ботом:\n'
                                        '/orel -  вызвать орловского помощника\n'
                                        '/pidorstat - пидорский рейтинг \n'
                                        '/start - инициализация бота\n'
                                        '/help - справка по боту\n'
                                        '/test - тестирование бота'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message('@suetologyorla', '''Бот уже инициализирован.
Я работаю по расписанию. Пидр дня назначается ежедневно 
в 11:00 по московскому времени
/help - справка по боту''')


def pstat():
    stat_file = open("статистика", 'r+')
    d0 = stat_file.read().split(sep='\n')
    d1 = [(int(d0[0]), "Филч"), (int(d0[1]), "Игорь"), (int(d0[2]), "Серега"), (int(d0[3]), "Саня"),
          (int(d0[4]), "Леха(Саня)"), (int(d0[5]), "Леха(Фитиль)"), (int(d0[6]), "Диман")]
    d1_sort = sorted(d1, reverse=True)
    stat_file.close()
    return (f'''РЕЙТИНГ ПИДАРАСОВ:
1. {d1_sort[0][1]} -----> {d1_sort[0][0]} раз(а)
2. {d1_sort[1][1]} -----> {d1_sort[1][0]} раз(а)
3. {d1_sort[2][1]} -----> {d1_sort[2][0]} раз(а)
4. {d1_sort[3][1]} -----> {d1_sort[3][0]} раз(а)
5. {d1_sort[4][1]} -----> {d1_sort[4][0]} раз(а)
6. {d1_sort[5][1]} -----> {d1_sort[5][0]} раз(а)
7. {d1_sort[6][1]} -----> {d1_sort[6][0]} раз(а)
Да здравствует наш чемпион {d1_sort[0][1]}! Его результативности 
может позавидовать Элтон Джон и другие Великие. Пожелаем
ему здоровья, успехов в личной жизни и новых побед.
/help - справка по боту''')


@bot.message_handler(commands=['pidorstat'])
def test(message):
    bot.send_message('@suetologyorla', pstat())


@bot.message_handler(commands=['test'])
def start(message):
    bot.send_message('@suetologyorla', '''Протестируй себя петушок...А моя работа давно проверена и отлажена.
/help - справка по боту''')


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(pidr, "cron", day_of_week='mon-sun', hour=8)
    scheduler.start()

    try:
        @bot.message_handler(commands=['orel'])
        def orel(message):
            bot.send_message('@suetologyorla', 'Орловский помощник..', reply_markup=kb1)
    except KeyboardInterrupt:
        pass

bot.polling()
