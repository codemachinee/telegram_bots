import telebot
from telebot import types

bot = telebot.TeleBot('BotApi')


@bot.message_handler(commands=['start'])
def start(message):
    start_file = open("Я.png", 'rb')
    bot.send_photo(message.chat.id, start_file)
    bot.send_message(message.chat.id, """Приветствую тебя прекрасная жена 👩🏻 легендарного мужа!👨🏻‍💻🦅🥷🏻
Я создан 👾 ради обеспечения твоего досуга пока муж отсутствует. В данной версии предлагается тест, направленный
на выявление уровня любви к мужу❤️. При успешном прихождении тебя ожидает сюрприз.🤩🤩🤩""""")
    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    but1 = types.KeyboardButton(text='Поехали🏄🏻‍♂️🏄🏻‍♂️!')
    but2 = types.KeyboardButton(text='Я не люблю мужа')
    kb1.add(but1, but2)
    bot.send_message(message.chat.id, '...', reply_markup=kb1)


@bot.message_handler(func=lambda x: x.text)
def chek_message(x):
    if x.text == 'Поехали🏄🏻‍♂️🏄🏻‍♂️!':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id, '''Умница❤️, правильный выбор хоть и по лезвию прошлась..''')
        but3 = types.KeyboardButton(text='2 яйца')
        but4 = types.KeyboardButton(text='3 яйца')
        but5 = types.KeyboardButton(text='4 яйца')
        but6 = types.KeyboardButton(text='5 яиц')
        kb2.add(but3, but4, but5, but6)
        bot.send_message(x.chat.id, '🤤🤤🤤Сколько яиц нужно для идеального завтрака мужа?🤤🤤🤤', reply_markup=kb2)
    elif x.text == 'Я не люблю мужа':
        file1 = open('собакасука.png', 'rb')
        bot.send_photo(x.chat.id, file1, '''БУДЕМ СЧИТАТЬ ЧТО ТЫ ПРОМАЗАЛА 😈😈😈😈 и спишем на невнимательность.
Дам тебе еще шанс, будь бдительнее!''')
    elif x.text == '3 яйца':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id, '''Молодчина❤️ в завтраках ты знаешь толк''')
        but3 = types.KeyboardButton(text='Моргенштерн')
        but4 = types.KeyboardButton(text='М.Круг')
        but5 = types.KeyboardButton(text='Таркан')
        but6 = types.KeyboardButton(text='Озон')
        kb2.add(but3, but4, but5, but6)
        bot.send_message(x.chat.id, 'Под трек какого исполнителя танцевала Настюха в конкурсе на нашей свадьбе?💃🏻',
                         reply_markup=kb2)
    elif x.text.startswith('2 яй') or x.text.startswith('4 яй') or x.text.startswith('5 яи'):
        file1 = open('кулак.png', 'rb')
        bot.send_photo(x.chat.id, file1, '''Родная, ты меня начинаешь расстраивать...🙄🙄🙄 Попробуй еще раз!''')
    elif x.text == 'Таркан':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id, '''Лучшая!!!🤩 Чувствуешь, вопросы усложняются?''')
        but3 = types.KeyboardButton(text='2 баночки')
        but4 = types.KeyboardButton(text='3 баночки')
        but5 = types.KeyboardButton(text='4 баночки')
        but6 = types.KeyboardButton(text='5 баночек')
        kb2.add(but3, but4, but5, but6)
        bot.send_message(x.chat.id, 'Сколько баночек меда муж-добытчик принес с работы?🐝🐝🐝', reply_markup=kb2)
    elif x.text.startswith('Морге') or x.text.startswith('М.Кр') or x.text.startswith('Оз'):
        file1 = open('photo_2022-04-27_20-38-19.jpg', 'rb')
        bot.send_photo(x.chat.id, file1, '''Ну ты даешь)) такое то не знать... Попробуй еще раз!''')
    elif x.text == '3 баночки':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id,
                         '''Правильно!!!🤩 Как говорил Великий..нужно ценить и помнить заботу мужа?🤌🏻🤌🏻🤌🏻''')
        but3 = types.KeyboardButton(text='Керч')
        but4 = types.KeyboardButton(text='Ялта')
        but5 = types.KeyboardButton(text='Севастополь')
        but6 = types.KeyboardButton(text='Анапа')
        kb2.add(but3, but4, but5, but6)
        file1 = open('мороженное.png', 'rb')
        bot.send_message(x.chat.id, 'Вижу сильно напряглась, дам тебе чуть чуть отдохнуть..'
                                    'Творческий вопрос.🎨 Где было сделано это фото??🍦🍦🍦', reply_markup=kb2)
        bot.send_photo(x.chat.id, file1)
    elif x.text.startswith('2 бан') or x.text.startswith('4 бан') or x.text.startswith('5 бан'):
        file1 = open('бигтести.png', 'rb')
        bot.send_photo(x.chat.id, file1, '''Мдаа...Вот она благодарность... Попробуй еще раз!🙄🙄🙄''')
    elif x.text == 'Анапа':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id,
                         '''Правильно!!!🤩 Как говорил Великий..нужно ценить и помнить моменты 
проведенные с мужем?🤌🏻🤌🏻🤌🏻''')
        but3 = types.KeyboardButton(text='Анна')
        but4 = types.KeyboardButton(text='Элизавета')
        but5 = types.KeyboardButton(text='Татьяна')
        but6 = types.KeyboardButton(text='Мария')
        kb2.add(but3, but4, but5, but6)
        bot.send_message(x.chat.id, 'Отдохнула? - Получай 👊🏻 Как звали всех женщин, в которых когда-либо влюблялся '
                                    'Эраст Петрович Фандорин??🕵🏻‍♂️🕵🏻‍♂️', reply_markup=kb2)
    elif x.text.startswith('Кер') or x.text.startswith('Ялт') or x.text.startswith('Севас'):
        file1 = open('мороженное.png', 'rb')
        bot.send_photo(x.chat.id, file1, '''Топографический кретинизм или склероз, что-то из двух... 
Попробуй еще раз!🙄🙄🙄''')
    elif x.text == 'Элизавета':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id,
                         '''Браво👏🏻👏🏻👏🏻 Апплодирую стоя, если ты конечно действительно знала, а не нагло гуглила..😈''')
        but3 = types.KeyboardButton(text='2007')
        but4 = types.KeyboardButton(text='2008')
        but5 = types.KeyboardButton(text='2009')
        but6 = types.KeyboardButton(text='2010')
        kb2.add(but3, but4, but5, but6)
        bot.send_message(x.chat.id, 'Вопрос такой.. Какого года наша машина??🚘🚘🚘', reply_markup=kb2)
    elif x.text.startswith('Анн') or x.text.startswith('Татья') or x.text.startswith('Мари'):
        file1 = open('photo_2022-04-27_20-38-19.jpg', 'rb')
        bot.send_photo(x.chat.id, file1, '''А кто говорил, что будет просто? Только не вздумай гуглить... 
Попробуй еще раз!🙄🙄🙄''')
    elif x.text == '2007':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id,
                         '''Верно👏🏻👏🏻👏🏻 Она бегала уже тогда, когда ты ходила в 4 класс.. 
Думай об этом когда оставляешь мусор в дверях😈''')
        but3 = types.KeyboardButton(text='левую')
        but4 = types.KeyboardButton(text='правую')
        but5 = types.KeyboardButton(text='среднюю')
        but6 = types.KeyboardButton(text='никогда ничего не подорачивает')
        kb2.add(but3, but4, but5, but6)
        bot.send_message(x.chat.id, '''Чуть-чуть отдохнем и вернемся к обыденному.. Какую ногу муж 
постоянно подворачивает??🦿🦿🦿''', reply_markup=kb2)
    elif x.text.startswith('2008') or x.text.startswith('2009') or x.text.startswith('2010'):
        file1 = open('кулак.png', 'rb')
        bot.send_photo(x.chat.id, file1, '''Любишь кататься люби и саночки любить... 
Попробуй еще раз!🙄🙄🙄''')
    elif x.text == 'правую':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id,
                         '''В точку👏🏻👏🏻👏🏻 Пишу с болью от представленного, но такова жизнь🙌🏻🙌🏻''')
        but3 = types.KeyboardButton(text='жопа')
        but4 = types.KeyboardButton(text='копчик')
        but5 = types.KeyboardButton(text='крестец')
        but6 = types.KeyboardButton(text='в голове у него что-то сломано')
        kb2.add(but3, but4, but5, but6)
        bot.send_message(x.chat.id, '''Еще из той же корзины.. что сломано у мужа??🏄🏻‍♂️🏄🏻‍♂️🏄🏻‍♂️''', reply_markup=kb2)
    elif x.text.startswith('леву') or x.text.startswith('средн') or x.text.startswith('никогда ничего'):
        file1 = open('бигтести.png', 'rb')
        bot.send_photo(x.chat.id, file1, '''Стыдно не знать, низко фантазировать... 
Попробуй еще раз!🙄🙄🙄''')
    elif x.text == 'крестец':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id,
                         '''В точку👏🏻👏🏻👏🏻 зато сейчас как новенькая🙌🏻🙌🏻''')
        but3 = types.KeyboardButton(text='кроп')
        but4 = types.KeyboardButton(text='полубокс')
        but5 = types.KeyboardButton(text='фейд')
        but6 = types.KeyboardButton(text='модельная')
        kb2.add(but3, but4, but5, but6)
        bot.send_message(x.chat.id, '''Как называется прическа мужа??💇🏻‍♂️💇🏻‍♂️💇🏻‍♂️''',
                         reply_markup=kb2)
    elif x.text.startswith('жоп') or x.text.startswith('копч') or x.text.startswith('в голове у него'):
        file1 = open('кулак.png', 'rb')
        bot.send_photo(x.chat.id, file1, '''Шутница чтоли, отвечай серьезно... 
Попробуй еще раз!🙄🙄🙄''')
    elif x.text == 'фейд':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id,
                         '''Что-то знаешь👏🏻👏🏻👏🏻 молодец!!!👍🏻👍🏻👍🏻''')
        but3 = types.KeyboardButton(text='Геракл')
        but4 = types.KeyboardButton(text='Атлант')
        but5 = types.KeyboardButton(text='Зевс')
        but6 = types.KeyboardButton(text='Гигант')
        kb2.add(but3, but4, but5, but6)
        bot.send_message(x.chat.id, '''Как муж просит называть его на публике??💁🏻‍♂️💁🏻‍♂️💁🏻‍♂️''',
                         reply_markup=kb2)
    elif x.text.startswith('кроп') or x.text.startswith('полубок') or x.text.startswith('модельн'):
        file1 = open('бигтести.png', 'rb')
        bot.send_photo(x.chat.id, file1, '''Мдаа.. Это же азы Дорогаяя... 
Попробуй еще раз!🙄🙄🙄''')
    elif x.text == 'Гигант':
        kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot.send_message(x.chat.id,
                         '''Верно, но ты почему то игнорируешь мои просьбы!!!🙄🙄🙄''')
        but3 = types.KeyboardButton(text='идут')
        but4 = types.KeyboardButton(text='не идут')
        but5 = types.KeyboardButton(text='мужу идет все')
        but6 = types.KeyboardButton(text='у него не растет')
        kb2.add(but3, but4, but5, but6)
        bot.send_message(x.chat.id, '''Идут ли мужу усы??👨🏻👨🏻👨🏻''',
                         reply_markup=kb2)
    elif x.text.startswith('Герак') or x.text.startswith('Атлан') or x.text.startswith('Зевс'):
        file1 = open('бигтести.png', 'rb')
        bot.send_photo(x.chat.id, file1, '''Мдаа.. Теперь ясно почему это не реализуется... 
Попробуй еще раз!🙄🙄🙄''')
    elif x.text == 'мужу идет все':
        kb2 = types.ReplyKeyboardRemove()
        bot.send_message(x.chat.id,
                         '''В точку, единственно возможный верный ответ!!!🙌🏻🙌🏻🙌🏻''')
        bot.send_message(x.chat.id, '''И так..Финальный вопрос от которого зависит добьешься ты победы или нет, 
заберешь золото этого Форта Боярда или останешься ни с чем. Вопрос никак не связан с мужем и имеет чисто логический
интерес.
    
Первый это первый, второй это десятый, а третий это второй. Первого победила сила гравитации, 
третий наруший все законы физики, где оказался второй??👨🏻👨🏻👨🏻 Ответ напиши на клавиатуре, всего 2 слова, 
первое - предлог. Удачи!''', reply_markup=kb2)
    elif x.text.startswith('не идут') or x.text.startswith('идут') or x.text.startswith('у него не рас'):
        file1 = open('бигтести.png', 'rb')
        bot.send_photo(x.chat.id, file1, '''Подумай хорошенько... 
Попробуй еще раз!🙄🙄🙄''')
    elif x.text.startswith('на труб') or x.text.startswith('На труб'):
        file_vid = open('IMG_1538.MOV', 'rb')
        bot.send_message(x.chat.id, '''🥇🎉🎊Умница, конечно же это детская загадка является ответом на загадку взрослую!"
"Твой заслуженный приз скоро появится...🥇🎉🎊''')
        bot.send_video(x.chat.id, file_vid)
    else:
        bot.send_message(x.chat.id, "Дорогая, ты либо отклоняешься от инструкций либо отвечаешь неверно.👾👾👾")


bot.polling()
