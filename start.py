"""
бот опроса соискателей о причинах отказа от позиции

@ author: vndanilchenko@gmail.com
"""



import telebot, os
import logging

# импортируем токены
try:
    token = os.environ['TG_TOKEN']
except:
    from private.token import token

bot = telebot.TeleBot(token=token)

# добавим логирование
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


REPLY_START = 'Привет, ты написал боту опроса соискателей\n'\
              '- узнать о функционале бота /whatyoucando\n' \
              '- пройти опрос /startpoll'

REPLY_WHOIS = 'я могу выполнить опрос по заранее заготовленному шаблону, если хочешь попроовать, жми /startpoll'

REPLY_POLL = 'тут будет опрос'

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('узнать функционал', 'начать опрос')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, REPLY_START, reply_markup=keyboard1)

# узнать о функционале бота
@bot.message_handler(commands=['whatyoucando'])
def start_message(message):
    bot.send_message(message.chat.id, REPLY_WHOIS)


# начать опрос

@bot.message_handler(commands=['startpoll'])
def first_question(message):
    question = 'вопрос 1 из 3: Укажите вакансию, на которую Вы претендовали';
    keyboard = telebot.types.InlineKeyboardMarkup();  # наша клавиатура
    key_1_1 = telebot.types.InlineKeyboardButton(text='Операционист-кассир', callback_data='1.1');  # кнопка «Да»
    keyboard.add(key_1_1);  # добавляем кнопку в клавиатуру
    key_1_2 = telebot.types.InlineKeyboardButton(text='Кредитный специалист', callback_data='1.2');
    keyboard.add(key_1_2);

    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    # bot.register_next_step_handler(message, second_question)
    # second_question(message)

# @bot.message_handler(content_types=['text'])
def second_question(message):
    question = 'вопрос 2 из 3: Укажите Ваш город';
    keyboard = telebot.types.InlineKeyboardMarkup();  # наша клавиатура
    key_2_1 = telebot.types.InlineKeyboardButton(text='Барнаул', callback_data='2.1');  # кнопка «Да»
    keyboard.add(key_2_1);  # добавляем кнопку в клавиатуру
    key_2_2 = telebot.types.InlineKeyboardButton(text='Воронеж', callback_data='2.2');
    keyboard.add(key_2_2);
    key_2_3 = telebot.types.InlineKeyboardButton(text='Зеленоград', callback_data='2.3');  # кнопка «Да»
    keyboard.add(key_2_3);  # добавляем кнопку в клавиатуру
    key_2_4 = telebot.types.InlineKeyboardButton(text='Казань', callback_data='2.4');
    keyboard.add(key_2_4);
    key_2_5 = telebot.types.InlineKeyboardButton(text='Колпино', callback_data='2.5');  # кнопка «Да»
    keyboard.add(key_2_5);  # добавляем кнопку в клавиатуру
    key_2_6 = telebot.types.InlineKeyboardButton(text='Комсомольск-на-Амуре', callback_data='2.6');
    keyboard.add(key_2_6);
    key_2_7 = telebot.types.InlineKeyboardButton(text='Королев', callback_data='2.7');  # кнопка «Да»
    keyboard.add(key_2_7);  # добавляем кнопку в клавиатуру
    key_2_8 = telebot.types.InlineKeyboardButton(text='Кострома', callback_data='2.8');
    keyboard.add(key_2_8);
    key_2_9 = telebot.types.InlineKeyboardButton(text='Кропоткин', callback_data='2.9');  # кнопка «Да»
    keyboard.add(key_2_9);  # добавляем кнопку в клавиатуру
    key_2_10 = telebot.types.InlineKeyboardButton(text='Лабинск', callback_data='2.10');
    keyboard.add(key_2_10);
    key_2_11 = telebot.types.InlineKeyboardButton(text='Можайск', callback_data='2.11');  # кнопка «Да»
    keyboard.add(key_2_11);  # добавляем кнопку в клавиатуру
    key_2_12 = telebot.types.InlineKeyboardButton(text='Москва', callback_data='2.12');
    keyboard.add(key_2_12);
    key_2_13 = telebot.types.InlineKeyboardButton(text='Находка', callback_data='2.13');  # кнопка «Да»
    keyboard.add(key_2_13);  # добавляем кнопку в клавиатуру
    key_2_14 = telebot.types.InlineKeyboardButton(text='Нижний Тагил', callback_data='2.14');
    keyboard.add(key_2_14);
    key_2_15 = telebot.types.InlineKeyboardButton(text='Одинцово', callback_data='2.15');  # кнопка «Да»
    keyboard.add(key_2_15);  # добавляем кнопку в клавиатуру
    key_2_16 = telebot.types.InlineKeyboardButton(text='Петропавловск-Камчатский', callback_data='2.16');
    keyboard.add(key_2_16);
    key_2_17 = telebot.types.InlineKeyboardButton(text='Санкт-Петербург', callback_data='2.17');  # кнопка «Да»
    keyboard.add(key_2_17);  # добавляем кнопку в клавиатуру
    key_2_18 = telebot.types.InlineKeyboardButton(text='Ульяновск', callback_data='2.18');
    keyboard.add(key_2_18);
    key_2_19 = telebot.types.InlineKeyboardButton(text='Тихорецк', callback_data='2.19');  # кнопка «Да»
    keyboard.add(key_2_19);  # добавляем кнопку в клавиатуру
    key_2_20 = telebot.types.InlineKeyboardButton(text='Элиста', callback_data='2.20');
    keyboard.add(key_2_20);
    key_2_21 = telebot.types.InlineKeyboardButton(text='Тюмень', callback_data='2.21');  # кнопка «Да»
    keyboard.add(key_2_21);  # добавляем кнопку в клавиатуру
    key_2_22 = telebot.types.InlineKeyboardButton(text='Пушкино', callback_data='2.22');
    keyboard.add(key_2_22);
    key_2_23 = telebot.types.InlineKeyboardButton(text='Ступино', callback_data='2.23');  # кнопка «Да»
    keyboard.add(key_2_23);  # добавляем кнопку в клавиатуру
    key_2_24 = telebot.types.InlineKeyboardButton(text='Тверь', callback_data='2.24');
    keyboard.add(key_2_24);
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    # bot.register_next_step_handler(message, third_question)
    # third_question(message)

# @bot.message_handler(content_types=['text'])
def third_question(message):
    question = 'вопрос 3 из 3: Уточните причины, почему Вам не подходит вакансия? (выберите один или несколько подходящих вариантов)';
    keyboard = telebot.types.InlineKeyboardMarkup();  # наша клавиатура
    key_3_1 = telebot.types.InlineKeyboardButton(text='Уже нашел работу', callback_data='3.1');  # кнопка «Да»
    keyboard.add(key_3_1);  # добавляем кнопку в клавиатуру
    key_3_2 = telebot.types.InlineKeyboardButton(text='Не интересен функционал вакансии', callback_data='3.2');
    keyboard.add(key_3_2);
    key_3_3 = telebot.types.InlineKeyboardButton(text='Не устраивает окладная часть', callback_data='3.3');  # кнопка «Да»
    keyboard.add(key_3_3);  # добавляем кнопку в клавиатуру
    key_3_4 = telebot.types.InlineKeyboardButton(text='Не устраивает совокупный доход', callback_data='3.4');
    keyboard.add(key_3_4);
    key_3_5 = telebot.types.InlineKeyboardButton(text='Не устраивает график работы', callback_data='3.5');  # кнопка «Да»
    keyboard.add(key_3_5);  # добавляем кнопку в клавиатуру
    key_3_6 = telebot.types.InlineKeyboardButton(text='Неудобное расположение места работы', callback_data='3.6');
    keyboard.add(key_3_6);
    key_3_7 = telebot.types.InlineKeyboardButton(text='Не понравились отзывы о работе в ХКФ Банке', callback_data='3.7');  # кнопка «Да»
    keyboard.add(key_3_7);  # добавляем кнопку в клавиатуру
    key_3_8 = telebot.types.InlineKeyboardButton(text='Решил пока не искать работу', callback_data='3.8');
    keyboard.add(key_3_8);
    key_3_9 = telebot.types.InlineKeyboardButton(text='Другое (укажите в комментарии)', callback_data='3.9');  # кнопка «Да»
    keyboard.add(key_3_9);  # добавляем кнопку в клавиатуру

    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    # bot.register_next_step_handler(message, bot.send_message(message.from_user.id, text='спасибо за участие'))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data[0]=='1':
        if call.data == "1.1": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'выбран вариант 1.1');
        elif call.data == "1.2":
            bot.send_message(call.message.chat.id, 'выбран вариант 1.2');
        second_question(call)
    elif call.data[0]=='2':
        if call.data == "2.1":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.1');
        elif call.data == "2.2":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.2');
        elif call.data == "2.3": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'выбран вариант 2.3');
        elif call.data == "2.4":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.4');
        elif call.data == "2.5":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.5');
        elif call.data == "2.6":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.6');
        elif call.data == "2.7": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'выбран вариант 2.7');
        elif call.data == "2.8":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.8');
        elif call.data == "2.9":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.9');
        elif call.data == "2.10":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.10');
        elif call.data == "2.11": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'выбран вариант 2.11');
        elif call.data == "2.12":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.12');
        elif call.data == "2.13":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.13');
        elif call.data == "2.14":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.14');
        elif call.data == "2.15": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'выбран вариант 2.15');
        elif call.data == "2.16":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.16');
        elif call.data == "2.17":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.17');
        elif call.data == "2.18":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.18');
        elif call.data == "2.19": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'выбран вариант 2.19');
        elif call.data == "2.20":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.20');
        elif call.data == "2.21":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.21');
        elif call.data == "2.22":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.22');
        elif call.data == "2.23": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'выбран вариант 2.23');
        elif call.data == "2.24":
            bot.send_message(call.message.chat.id, 'выбран вариант 2.24');
        third_question(call)
    elif call.data[0]=='3':
        if call.data == "3.1":
            bot.send_message(call.message.chat.id, 'выбран вариант 3.1');
        elif call.data == "3.2":
            bot.send_message(call.message.chat.id, 'выбран вариант 3.2');
        elif call.data == "3.3": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'выбран вариант 3.3');
        elif call.data == "3.4":
            bot.send_message(call.message.chat.id, 'выбран вариант 3.4');
        elif call.data == "3.5":
            bot.send_message(call.message.chat.id, 'выбран вариант 3.6');
        elif call.data == "3.6":
            bot.send_message(call.message.chat.id, 'выбран вариант 3.6');
        elif call.data == "3.7":
            bot.send_message(call.message.chat.id, 'выбран вариант 3.7');
        elif call.data == "3.8":
            bot.send_message(call.message.chat.id, 'выбран вариант 3.8');
        elif call.data == "3.9":
            bot.send_message(call.message.chat.id, 'выбран вариант 3.9');
        bot.send_message(call.message.chat.id, 'спасибо за уделенное время, вы помогаете нашим сервисам стать лучше');

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower()=='узнать функционал':
        bot.send_message(message.chat.id, REPLY_START)
    elif message.text.lower()=='начать опрос':
        start_message(message)


bot.polling(none_stop=True, interval=0)