import telebot
from telebot import types

bot = telebot.TeleBot('5548312799:AAH6DnHNxIsk4grDhqZsm8Qh94WFoewT9NQ')


@bot.message_handler(commands=['start', 'he'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler()
# def get_user_text(message):
#   if message.text == "Hello":
#        bot.send_message(message.chat.id, "и тебе привет!",parse_mode='html')
#   elif message.text =="id":
#       bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
#   elif message.text == "photo":
#      photo = open('icon.png.jpg', 'rb')
#       bot.send_photo(message.chat.id, photo)
#   else:
#      bot.send_message(message.chat.id, "я тебя не понимаю" ,parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("посетить веб сайт", url="https://www.youtube.com/watch?v=_daTfgc4u3k))
    bot.send_message(message.chat.id, 'крутая музыка!', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton('веб сайт',")
    start = types.KeyboardButton('start')



    markup.add(website, start)
    bot.send_message(message.chat.id, 'крутая музыка!', reply_markup=markup)


bot.polling(none_stop=True)
