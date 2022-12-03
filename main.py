import telebot
import datetime
from settings import token, bot_url

bot = telebot.TeleBot(token)

print(f"Бот работает. Перейди по ссылке {bot_url}")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}</b>. Чем я могу помочь?\n" \
           "Посмотреть список команд: \n/help"
    bot.send_message(message.chat.id, mess, parse_mode="html")


@bot.message_handler(commands=["help"])
def help(message):
    mess = "Список команд\n" \
           "1. Показать время - /time\n" \
           "2. Показать дату - /date\n"
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

@bot.message_handler()
def explicitContent(message):
    if message.text == "ПОШЕЛ НАХУЙ" or message.text == "пошел нахуй":
        mess = "Сам иди нахуй"
        bot.send_message(message.chat.id, mess, parse_mode="html")
    else:
        mess = "Не пон\n" \
               "Обратитесь к /help"
        bot.send_message(message.chat.id, mess, parse_mode="html")

bot.polling(none_stop=True)



print("Бот остановлен")