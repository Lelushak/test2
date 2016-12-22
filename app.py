# -*- coding: utf-8 -*-

import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)
    
@bot.message_handler(commands=["geophone"])
def geophone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Test phone", request_contact=True)
    button_geo = types.KeyboardButton(text="Test place", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, Blablabla", reply_markup=keyboard)

@bot.message_handler(commands=["testkey"])
def ReplyKeyboardHide()     
    markup = types.ReplyKeyboardMarkup()
    markup.row('Numerics', 'Symbols')
    markup.row('Special')
    bot.send_message(message.chat.id, "Choose:", reply_markup=markup)



if __name__ == '__main__':
     bot.polling(none_stop=True)	
