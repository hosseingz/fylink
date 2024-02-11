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


@bot.message_handler(content_types=['video'])
def video_validation(message):
    id = message.video.file_id
    chat_id = message.chat.id
    # Todo tabligat ezafala
    if message.video.file_size > 314572800:
        bot.reply_to(message, 'فایل شما باید حجمش کمتر از 300 مگ باشد')
    else:
        # if users active downloads bigger than 3, its return the False
        if not (ms := check_user_downloads(str(chat_id), id)):
            try:
                # get file list
                Files = requests.get(url="http://127.0.0.1:8000/bot/Commends/files/")
                # if file was downloaded, its return True
                if file := was_it_linked(Files, id):
                    bot.reply_to(message, f'لینک دانلود شما :\n {file["url"]}')
                else:

                    file_info = bot.get_file(id)
                    data = {
                        'chat_id': chat_id,
                        'file_id': id,
                        'file_name': message.video.file_name,
                        'file_extension': mimetypes.guess_extension(message.video.mime_type),
                        'file_path': file_info.file_path,
                        'file_size': file_info.file_size / (1024 ** 2)
                    }
                    response = requests.post(url="http://127.0.0.1:8000/bot/Commends/add-to-download-list/", data=data)

                    if response.status_code == "200":
                        bot.reply_to(message, 'به لیست دانلود اضافه شد !!!')
            except:
                bot.reply_to(message, ms)
        else:
            bot.reply_to(message, f'شما هم اکنون سه تا فایل در صف دانلود دارید. لطفا صبر کنید')


@bot.message_handler(content_types=['document'])
def document_validation(message):
    id = message.document.file_id
    chat_id = message.chat.id
    # Todo tabligat ezafala
    if message.document.file_size > 314572800:
        bot.reply_to(message, 'فایل شما باید حجمش کمتر از 300 مگ باشد')
    else:
        # if users active downloads bigger than 3, its return the False
        if not (ms := check_user_downloads(str(chat_id), id)):
            try:
                # get file list
                Files = requests.get(url="http://127.0.0.1:8000/bot/Commends/files/")
                # if file was downloaded, its return True
                if file := was_it_linked(Files, id):
                    bot.reply_to(message, f'لینک دانلود شما :\n {file["url"]}')
                else:

                    file_info = bot.get_file(id)
                    data = {
                        'chat_id': chat_id,
                        'file_id': id,
                        'file_name': message.document.file_name,
                        'file_extension': mimetypes.guess_extension(message.document.mime_type),
                        'file_path': file_info.file_path,
                        'file_size': file_info.file_size / (1024 ** 2)
                    }
                    response = requests.post(url="http://127.0.0.1:8000/bot/Commends/add-to-download-list/", data=data)

                    if response.status_code == "200":
                        bot.reply_to(message, 'به لیست دانلود اضافه شد !!!')
            except:
                bot.reply_to(message, ms)
        else:
            bot.reply_to(message, f'شما هم اکنون سه تا فایل در صف دانلود دارید. لطفا صبر کنید')


@bot.message_handler(content_types=['audio'])
def audio_validation(message):
    id = message.audio.file_id
    chat_id = message.chat.id
    # Todo tabligat ezafala
    if message.document.file_size > 314572800:
        bot.reply_to(message, 'فایل شما باید حجمش کمتر از 300 مگ باشد')
    else:
        # if users active downloads bigger than 3, its return the False
        if not (ms := check_user_downloads(str(chat_id), id)):
            try:
                # get file list
                Files = requests.get(url="http://127.0.0.1:8000/bot/Commends/files/")
                # if file was downloaded, its return True
                if file := was_it_linked(Files, id):
                    bot.reply_to(message, f'لینک دانلود شما :\n {file["url"]}')
                else:

                    file_info = bot.get_file(id)
                    data = {
                        'chat_id': chat_id,
                        'file_id': id,
                        'file_name': message.audio.file_name,
                        'file_extension': mimetypes.guess_extension(message.audio.mime_type),
                        'file_path': file_info.file_path,
                        'file_size': file_info.file_size / (1024 ** 2)
                    }
                    response = requests.post(url="http://127.0.0.1:8000/bot/Commends/add-to-download-list/", data=data)

                    if response.status_code == "200":
                        bot.reply_to(message, 'به لیست دانلود اضافه شد !!!')
            except:
                bot.reply_to(message, ms)
        else:
            bot.reply_to(message, f'شما هم اکنون سه تا فایل در صف دانلود دارید. لطفا صبر کنید')







# message = request.message
#
# file = message.document if message.document else \
#     message.video if message.video else message.audio if message.audio else None
#
# file_id = file.file_id
# file_info = bot.get_file(file_id)
# file_path = file_info.file_path
# file_name = file_path.rsplit('/')[-1]
# file_size = file_info.file_size
# file_extension = mimetypes.guess_extension(file.mime_type)
#
# download_url = f"https://api.telegram.org/file/bot{bot.token}/{file_path}"
# response = requests.get(download_url)


