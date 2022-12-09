import telebot
import datetime
from settings import token, bot_url

bot = telebot.TeleBot(token)

print(f"Ботработает. Перейди по ссылке {bot_url}")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}</b>. Чем я могу помочь?\n" \
           "Посмотреть список команд: \n/help"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["help"])
def help(message):
    mess = "Список команд\n" \
           "1.\U0001F92B Показать время - /time\n" \
           "2. Показать дату - /date\n" \
           "3. Где поесть - /eat\n" \
           "4. Расписание - /sheldule\n" \
           "5. Туалеты - /toilets\n" \
           "6. Расписание звонков - /hour\n" \
           "7. Шаблоны для отчетов - /practice\n" \
           "8. Оставить отзыв в 2Gis - /map\n" \
           "9. компютерные классы - /computers\n"


    bot.send_message(message.chat.id, mess, parse_mode="html")



@bot.message_handler(commands=["time"])
def getTime(message):
    _time = datetime.datetime.now()
    mess = f"Сейчас: {_time.hour}:{_time.minute}"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["date"])
def getDate(message):
    _date = datetime.datetime.now()
    mess = f"Сегодня: {_date.day}/{_date.month}/{_date.year}"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["eat"])
def start(message):
    mess = f"4 этаж,Буффет\n" \
           "Посмотреть список команд: \n/help"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["sheldule"])
def start(message):
    mess = f"1-Математика\n2- Физика\n3-История\n " \
           "Посмотреть список команд: \n/help"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["toilets"])
def start(message):
    mess = f"Мужские-4,5,7\n" \
           f"Женские-3,6\n" \
           "Посмотреть список команд: \n/help"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["hour"])
def start(message):
    mess = f"1 смена\n" \
            f"1 пара 8:00-9:20\n" \
               f"2 пара 9:30-10:50\n" \
               f"3 пара 11:00-12:20\n" \
               f"2 смена\n" \
               f"1 пара 13:30-14:50\n" \
               f"2 пара 15:00-16:20\n" \
               f"3 пара 16:30-17:50\n" \
               "Посмотреть список команд: \n/help"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=['practice'])
def sendFile(message):
    file = open('./practice/Отчет ИСД1-20Р.docx', 'rb')
    _mess = "Отправка файла"
    bot.send_message(message.chat.id, _mess, parse_mode="html")
    assert isinstance(file, object)
    bot.send_document(message.chat.id, file)

@bot.message_handler(commands=["map"])
def start(message):
        mess = f"https://go.2gis.com/2sdi3\n" \
               "Посмотреть список команд: \n/help"
        bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["computers"])
def start(message):
    mess = f"4 этаж\n" \
            f"403\n" \
               f"404\n" \
               f"405\n" \
               f"408\n" \
               f"410\n" \
               f"5 этаж\n" \
               f"502\n" \
           f"504\n" \
           f"505\n" \
           f"506\n" \
           f"508\n" \
           f"509B\n" \
               "Посмотреть список команд: \n/help"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler()
def explicitContent(message):
    if message.text == "Привет" or message.text == "Hi":
        mess = "Здарова, че надо? "
        bot.send_message(message.chat.id, mess, parse_mode="html")

    elif message.text == "Как дела?" or message.text == "чо на":
        mess = "Хорошо сам как?"
        bot.send_message(message.chat.id, mess, parse_mode="html")

    elif message.text == "Теймур лох" or message.text == "Ты даун":
        mess = "т. RIP BOZO \U0001F976 \U0001F976 \U0001F976"
        bot.send_message(message.chat.id, mess, parse_mode="html")

    elif message.text == "Ало это кто?" or message.text == "Але это кто?":
        mess = "Это он хехехе \U0001F608"
        bot.send_message(message.chat.id, mess, parse_mode="html")
    else:
        mess = "Не пон\n" \
               "Обратитесь к \n/help"
        bot.send_message(message.chat.id, mess, parse_mode="html")

bot.polling(none_stop=True)



print("Бот остановлен")