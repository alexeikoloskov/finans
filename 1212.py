import robot
import telebot
from telebot import types

bot = telebot.TeleBot('1364526508:AAElJt4zNg63ViKX07ogx1fCjy3OAImiSqo')
bot.polling(none_stop=True, interval=0)

name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message('Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/info':
#         keyboard = types.InlineKeyboardMarkup();  # наша клавиатура
#         key_get_one_instrument = types.InlineKeyboardButton(text='Получить конкретный инструмент',
#                                                             callback_data='yes');  # кнопка «Да»
#         keyboard.add(key_get_one_instrument);  # добавляем кнопку в клавиатуру
#         key_get_all_instrument = types.InlineKeyboardButton(text='Пока не работает((', callback_data='no');
#         keyboard.add(key_get_all_instrument);
#         key_get_one_operation = types.InlineKeyboardButton(text='Получить 1 операцию', callback_data='no');
#         keyboard.add(key_get_one_operation);
#         key_get_all_operation = types.InlineKeyboardButton(text='Получить все операции', callback_data='no');
#         keyboard.add(key_get_all_operation);
#         key_get_all_operation_in_data = types.InlineKeyboardButton(text='Получить операции за конкретный период', callback_data='no');
#         keyboard.add(key_get_all_operation_in_data);
#         question =('Че надо?')
#         bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#         # bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
#     else:
#         bot.send_message(message.from_user.id, 'Напиши /info')
#
#
# # def get_name(message): #получаем фамилию
# #
# #     bot.send_message('Сколько тебе лет?')
# #     bot.register_next_step_handler(message, get_age)
# # def get_surname(message):
# #
# #
# # def get_age(message):
