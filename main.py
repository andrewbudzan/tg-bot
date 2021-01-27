# author: andrii budzan
import os
import time
import telebot
import logging

from dotenv import load_dotenv

load_dotenv(override=True)

bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))
logger = telebot.logger
log_level = os.environ.get('LOG_LEVEL')
if log_level == 'INFO':
    telebot.logger.setLevel(logging.INFO)  # Outputs debug messages to console.
elif log_level == 'DEBUG':
    telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"I'm bot. Hello, {message.from_user.first_name}!")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, f"Sorry, {message.from_user.first_name}, I can't help you at the moment...")


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    text = message.text.lower()
    user = message.from_user
    if text == 'hello':
        bot.send_message(user.id, f'Hello {user.first_name}!')
    elif text == 'time':
        bot.send_message(user.id, f'{time.strftime("%H:%M:%S", time.gmtime())}')
    elif text == 'my_id':
        bot.send_message(user.id, f'{user.id}')
    elif text == 'my_data':
        bot.send_message(user.id, f'{user.__dict__}')
    elif text == 'date':
        bot.send_message(user.id, f'{time.strftime("%A, %d %B %Y", time.gmtime())}')
    elif text == 'datetime':
        bot.send_message(user.id, f'{time.strftime("%A, %d %B %Y %H:%M:%S +0000", time.gmtime())}')
    elif text == 'date_full':
        bot.send_message(user.id, f'{time.strftime("%c", time.gmtime())}')
    else:
        bot.send_message(user.id, f"Sorry, I don't understand you!")


def start_bot():
    bot.polling(none_stop=True)
