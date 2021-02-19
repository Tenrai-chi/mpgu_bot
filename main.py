import telebot

# Создание бота
bot = telebot.TeleBot('1699324423:AAHu5a2Q3z7kLLcye41btVJAnLLW1ZxmW4E')


# декоратор, который реагирует на /start
@bot.message_handler(commands=['start'])
def start_message(message):
    start = open('start.txt', 'r', encoding='utf-8')
    a = ''
    for row in start:
        a += row
    start.close()
    bot.send_message(message.chat.id, f"{a}")


# декоратор, который реагирует на /help
@bot.message_handler(commands=['help'])
def help_message(message):
    help_ = open('help.txt', 'r', encoding='utf-8')
    h = ''
    for row in help_:
        h += row
    help_.close()
    bot.send_message(message.chat.id, f"{h}")


# декоратор, который реагирует на /student
@bot.message_handler(commands=['student'])
def student_message(message):
    student = open('student.txt', 'r', encoding='utf-8')
    stud = ''
    for row in student:
        stud += row
    student.close()
    bot.send_message(message.chat.id, f"{stud}")


@bot.message_handler(commands=['aspirant'])
def aspirant_message(message):
    aspirant = open('aspirant.txt', 'r', encoding='utf-8')
    asp = ''
    for row in aspirant:
        asp += row
    aspirant.close()
    bot.send_message(message.chat.id, f"{asp}")


@bot.message_handler(commands=['zachislenya'])
def zachislenya_message(message):
    zach = open('zachislenya.txt', 'r', encoding='utf-8')
    z = ''
    for row in zach:
        z += row
    zach.close()
    bot.send_message(message.chat.id, f"{z}")


# Электронные ресурсы
@bot.message_handler(commands=['website'])
def website_message(message):
    web = open('website.txt', 'r', encoding='utf-8')
    w = ''
    for row in web:
        w += row
    web.close()
    bot.send_message(message.chat.id, f"{w}")


# Информация для аспирантов
@bot.message_handler(commands=['magistr'])
def magistr_message(message):
    magistr = open('magistr.txt', 'r', encoding='utf-8')
    mag = ''
    for row in magistr:
        mag += row
    magistr.close()
    bot.send_message(message.chat.id, f"{mag}")


# Приемная комиссия
@bot.message_handler(commands=['priem_com'])
def priem_com(message):
    com = open('priem_com.txt', 'r', encoding='utf-8')
    c = ''
    for row in com:
        c += row
    com.close()
    bot.send_message(message.chat.id, f"{c}")


# декоратор, который реагирует на текст
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'люблю мпгу' or message.text.lower() == 'люблю' or message.text.lower() == 'обожаю мпгу' or message.text.lower() == 'любимый мпгу':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALYuGAs8Hevz0h2HMzn_O5EPeLLTgUXAAICAAM7YCQUoMJLdBA-ZR4eBA')



bot.polling()