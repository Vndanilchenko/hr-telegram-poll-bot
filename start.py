"""
бот опроса соискателей о причинах отказа от позиции

@ author: vndanilchenko@gmail.com
"""



import telebot, os
import logging
import sqlite3, json, io

# импортируем токены
try:
    token = os.environ['TG_TOKEN']
except:
    from private.token import token


# импортируем id админа
try:
    token = os.environ['TG_ADMIN_ID']
except:
    from private.token import admin_id

bot = telebot.TeleBot(token=token)

# добавим логирование
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


REPLY_START = 'Привет, ты написал боту опроса соискателей\n'\
              '- узнать о функционале бота /whatyoucando\n' \
              '- пройти опрос /startpoll'

REPLY_WHOIS = 'я могу выполнить опрос по заранее заготовленному шаблону, если хочешь попроовать, жми /startpoll'

REPLY_POLL = 'тут будет опрос'

# если флаг=1, значит анкета закончена
FLAG_END_POLL = 0
# если флаг=1, значит клиент выбрал из причин "другое" и далее мы будем считать его текст комментарием к вопросу
FLAG_ELSE_REASON = 0
# будем заполнять эту переменную всеми фразами клиента, когда FLAG_ELSE_REASON!=1
comment = ''
# запишем комментарий на причину "другое" отказа от позиции
comment_else = ''
# ответы
respone_1 = ''
respone_2 = ''
respone_3 = ''

# настройки in memory бд
conn = sqlite3.connect(":memory:", check_same_thread=False)
cursor = conn.cursor()

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('узнать функционал', 'начать опрос')

# приветственное сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, REPLY_START, reply_markup=keyboard1)

# узнать о функционале бота
@bot.message_handler(commands=['whatyoucando'])
def whatyoucando(message):
    bot.send_message(message.chat.id, REPLY_WHOIS)



def check_user_data(message):
    sql = "SELECT * FROM users where chatid={}".format(message.chat.id)
    cursor.execute(sql)
    data = cursor.fetchone()  # or use fetchone()
    print(data)
    # if data.shape[0]==0:
    #     cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", data)
    # except Exception:
    #     # data = await get_data()
    #     # cursor.execute("CREATE TABLE users (chatid INTEGER , name TEXT, click INTEGER, state INTEGER)")
    #     cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", data)
    #     conn.commit()
    #     sql = "SELECT * FROM users where chatid={}".format(message.chat.id)
    #     cursor.execute(sql)
    #     data = cursor.fetchone()  # or use fetchone()

# начать опрос
@bot.message_handler(commands=['startpoll'])
def first_question(message):

    check_user_data(message)

    question = 'вопрос 1 из 3: Укажите вакансию, на которую Вы претендовали';
    keyboard = telebot.types.InlineKeyboardMarkup();  # наша клавиатура
    key_1_1 = telebot.types.InlineKeyboardButton(text='Операционист-кассир', callback_data='1.1');  # кнопка «Да»
    keyboard.add(key_1_1);  # добавляем кнопку в клавиатуру
    key_1_2 = telebot.types.InlineKeyboardButton(text='Кредитный специалист', callback_data='1.2');
    keyboard.add(key_1_2);

    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    # bot.register_next_step_handler(message, second_question)

def second_question(message):
    question = 'вопрос 2 из 3: Укажите Ваш город';
    keyboard = telebot.types.InlineKeyboardMarkup();  # клавиатура
    key_2_1 = telebot.types.InlineKeyboardButton(text='Барнаул', callback_data='2.1');
    keyboard.add(key_2_1);  # добавляем кнопку в клавиатуру
    key_2_2 = telebot.types.InlineKeyboardButton(text='Воронеж', callback_data='2.2');
    keyboard.add(key_2_2);
    key_2_3 = telebot.types.InlineKeyboardButton(text='Зеленоград', callback_data='2.3');
    keyboard.add(key_2_3);
    key_2_4 = telebot.types.InlineKeyboardButton(text='Казань', callback_data='2.4');
    keyboard.add(key_2_4);
    key_2_5 = telebot.types.InlineKeyboardButton(text='Колпино', callback_data='2.5');
    keyboard.add(key_2_5);
    key_2_6 = telebot.types.InlineKeyboardButton(text='Комсомольск-на-Амуре', callback_data='2.6');
    keyboard.add(key_2_6);
    key_2_7 = telebot.types.InlineKeyboardButton(text='Королев', callback_data='2.7');
    keyboard.add(key_2_7);
    key_2_8 = telebot.types.InlineKeyboardButton(text='Кострома', callback_data='2.8');
    keyboard.add(key_2_8);
    key_2_9 = telebot.types.InlineKeyboardButton(text='Кропоткин', callback_data='2.9');
    keyboard.add(key_2_9);
    key_2_10 = telebot.types.InlineKeyboardButton(text='Лабинск', callback_data='2.10');
    keyboard.add(key_2_10);
    key_2_11 = telebot.types.InlineKeyboardButton(text='Можайск', callback_data='2.11');
    keyboard.add(key_2_11);
    key_2_12 = telebot.types.InlineKeyboardButton(text='Москва', callback_data='2.12');
    keyboard.add(key_2_12);
    key_2_13 = telebot.types.InlineKeyboardButton(text='Находка', callback_data='2.13');
    keyboard.add(key_2_13);
    key_2_14 = telebot.types.InlineKeyboardButton(text='Нижний Тагил', callback_data='2.14');
    keyboard.add(key_2_14);
    key_2_15 = telebot.types.InlineKeyboardButton(text='Одинцово', callback_data='2.15');
    keyboard.add(key_2_15);
    key_2_16 = telebot.types.InlineKeyboardButton(text='Петропавловск-Камчатский', callback_data='2.16');
    keyboard.add(key_2_16);
    key_2_17 = telebot.types.InlineKeyboardButton(text='Санкт-Петербург', callback_data='2.17');
    keyboard.add(key_2_17);
    key_2_18 = telebot.types.InlineKeyboardButton(text='Ульяновск', callback_data='2.18');
    keyboard.add(key_2_18);
    key_2_19 = telebot.types.InlineKeyboardButton(text='Тихорецк', callback_data='2.19');
    keyboard.add(key_2_19);
    key_2_20 = telebot.types.InlineKeyboardButton(text='Элиста', callback_data='2.20');
    keyboard.add(key_2_20);
    key_2_21 = telebot.types.InlineKeyboardButton(text='Тюмень', callback_data='2.21');
    keyboard.add(key_2_21);
    key_2_22 = telebot.types.InlineKeyboardButton(text='Пушкино', callback_data='2.22');
    keyboard.add(key_2_22);
    key_2_23 = telebot.types.InlineKeyboardButton(text='Ступино', callback_data='2.23');
    keyboard.add(key_2_23);
    key_2_24 = telebot.types.InlineKeyboardButton(text='Тверь', callback_data='2.24');
    keyboard.add(key_2_24);

    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

def third_question(message):
    question = 'вопрос 3 из 3: Уточните причины, почему Вам не подходит вакансия? (выберите один или несколько подходящих вариантов)';
    keyboard = telebot.types.InlineKeyboardMarkup();  # клавиатура
    key_3_1 = telebot.types.InlineKeyboardButton(text='Уже нашел работу', callback_data='3.1');
    keyboard.add(key_3_1);  # добавляем кнопку в клавиатуру
    key_3_2 = telebot.types.InlineKeyboardButton(text='Не интересен функционал вакансии', callback_data='3.2');
    keyboard.add(key_3_2);
    key_3_3 = telebot.types.InlineKeyboardButton(text='Не устраивает окладная часть', callback_data='3.3');
    keyboard.add(key_3_3);
    key_3_4 = telebot.types.InlineKeyboardButton(text='Не устраивает совокупный доход', callback_data='3.4');
    keyboard.add(key_3_4);
    key_3_5 = telebot.types.InlineKeyboardButton(text='Не устраивает график работы', callback_data='3.5');
    keyboard.add(key_3_5);
    key_3_6 = telebot.types.InlineKeyboardButton(text='Неудобное расположение места работы', callback_data='3.6');
    keyboard.add(key_3_6);
    key_3_7 = telebot.types.InlineKeyboardButton(text='Не понравились отзывы о работе в ХКФ Банке', callback_data='3.7');
    keyboard.add(key_3_7);
    key_3_8 = telebot.types.InlineKeyboardButton(text='Решил пока не искать работу', callback_data='3.8');
    keyboard.add(key_3_8);
    key_3_9 = telebot.types.InlineKeyboardButton(text='Другое (укажите в комментарии)', callback_data='3.9');
    keyboard.add(key_3_9);

    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    # bot.register_next_step_handler(message, bot.send_message(message.from_user.id, text='спасибо за участие'))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global respone_1, respone_2, respone_3, FLAG_END_POLL, FLAG_ELSE_REASON
    # сделаем отдельную обработку на каждый блок вопросов
    # call.data это callback_data, которую мы указали при объявлении кнопки
    if call.data[0]=='1':
        respone_1 = call.data
        bot.send_message(call.message.chat.id, 'выбран вариант: ' + call.data);
        second_question(call)
    elif call.data[0]=='2':
        respone_2 = call.data
        bot.send_message(call.message.chat.id, 'выбран вариант: ' + call.data);
        third_question(call)
    elif call.data[0]=='3':
        respone_3 = call.data
        if call.data == "3.9":
            FLAG_ELSE_REASON = 1
        bot.send_message(call.message.chat.id, 'выбран вариант: ' + call.data);
        FLAG_END_POLL = 1
        if not FLAG_ELSE_REASON:
            final_message(call.message.chat.id, True)

def final_message(chat_id, final=False):
    # bot.send_message(chat_id, ('ваши ответы: ', respone_1, respone_2, respone_3, comment_else, comment))
    bot.send_message(chat_id, 'ваши ответы: ' + respone_1 + ' | ' + respone_2 + ' | ' + respone_3 + ' | ' + comment_else + ' | ' + comment)
    if final:
        bot.send_message(chat_id, 'спасибо за уделенное время, вы помогаете нашим сервисам стать лучше');

@bot.message_handler(content_types=['text'])
def send_text(message):
    global FLAG_ELSE_REASON, comment, comment_else
    if message.text.lower()=='admin create db' and str(message.from_user.id)==admin_id:
        cursor.execute("SELECT * FROM users ")
        data = cursor.fetchall()
        if len(data)==0:
            cursor.execute("CREATE TABLE users (chatid INTEGER, response_1 TEXT, response_2 TEXT, response_3 TEXT, "
                           "comment_else TEXT, comment TEXT);")
            cursor.execute("INSERT INTO users VALUES (123, 'resp1', 'resp2', 'resp3', 'comment_else', 'comment');")
                           # "INSERT INTO users VALUES ({}, {}, {}, {}, {}, {})".format(str(message.from_user.id), 'test_response_1',\
                           #                                                                'test_response_2', 'test_response_3',\
                           #                                                                'test_comment_else', 'test_comment_total',))
            # cursor.execute("INSERT INTO users VALUES ({}, {}, {}, {}, {}, {});".format(str(message.from_user.id), 'response_1',
            #                                                                               'response_2', 'response_3',
            #                                                                               'comment_else', 'comment_total'))
            conn.commit()
            print('database is created')
            bot.send_message(message.from_user.id, 'database is created')
        else:
            print('database is created')
            bot.send_message(message.from_user.id, 'database exists')
    elif message.text.lower() == 'admin export db' and str(message.from_user.id) == admin_id:
        cursor.execute("SELECT * FROM users ")
        data = cursor.fetchall()
        str_data = json.dumps(data)
        bot.send_document(message.chat.id, io.StringIO(str_data))
        # bot.send_message(message.chat.id, 'admin_id = {}'.format(message.chat.id))
        # bot.send_message(message.chat.id, 'config_id = {}'.format(message.message_id + 1))
        print('database is exported')
    if message.text.lower()=='узнать функционал':
        bot.send_message(message.chat.id, REPLY_START)
    elif message.text.lower()=='начать опрос':
        first_question(message)
    elif FLAG_ELSE_REASON == 1:
        comment_else = message.text
        bot.send_message(message.chat.id, message.text)
        FLAG_ELSE_REASON = 2
    elif FLAG_ELSE_REASON == 2:
        comment += message.text + ';'
        bot.send_message(message.chat.id, "мы учтем ваш комментарий: " + message.text)
        final_message(message.chat.id, True)
    elif any(map( lambda x: x in message.text.lower(), ['пока', 'свидан', 'встреч'])):
        comment += message.text + ';'
        bot.send_message(message.chat.id, "мы учтем ваш комментарий: " + message.text)
        final_message(message.chat.id, True)
    else:
        comment += message.text + ';'
        bot.send_message(message.chat.id, "мы учтем ваш комментарий: " + message.text)
        final_message(message.chat.id)



bot.polling(none_stop=True, interval=0)