import os
import time
import telebot
import requests
import mimetypes
import threading
import schedule
from Conf import *
from utils import *
import requests
import json

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    username = message.from_user.username
    if username is not None:
        username = f'{message.from_user.first_name} {message.from_user.last_name}'

    response = 204
    for i in range(5):
        try:
            response = requests.get('http://127.0.0.1:8000/bot/Commends/new-user/',
                                    params={'chat_id': chat_id, 'username': username})

            break
        except requests.ConnectTimeout:
            bot.send_message("OZ CHAT ID YADA CANAL", 'ConnectTimeout')
            time.sleep(0.3)
        except requests.ConnectionError:
            bot.send_message("OZ CHAT ID YADA CANAL", 'ConnectionError')
            time.sleep(0.3)

    if json.loads(response.text) == 200:
        bot.reply_to(message, "شما استارت زدید!")  # Todo matnhasho edit kon hatman

    # Todo shisheyi
