import datetime
from telebot import types
import requests

from Conf import *


class Keyboard(types.ReplyKeyboardMarkup):
    def __init__(self, commands, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for command in commands:
            button = types.KeyboardButton(command)
            self.add(button)


# Todo test beshe
def check_user_downloads(chat_id: str, file_id:str):
    download_list = requests.post('http://127.0.0.1:8000/bot/Commends/download-list/').json()

    count = list(filter(lambda i: i['chat_id'] == chat_id, download_list)).__len__()
    # that count display  users active downloads count

    if file_id in [item['file']['file_id'] for item in download_list]:
        message = 'این فایل هم اکنون در صف دانلود است, شما نمیتوانید دوباره فروارد بکنید'
    elif count >= 3:
        message = f'شما هم اکنون سه تا فایل در صف دانلود دارید. لطفا صبر کنید'
    else:
        message = ''

    return message


def was_it_linked(files, id):
    for file in files:
        if file['file_id'] == id:
            return file
    return False


def add_to_queue(request, request_queue, bot):
    request_queue.append(request)

    message = request.message

    if len(request_queue) > 1:
        bot.reply_to(message, "درخواست شما در صف دانلود قرار گرفت")
        bot.send_message(message.chat.id, f'موقعیت درخواست شما در صف :{len(request_queue) - 1}')
    else:
        bot.reply_to(message, 'درحال پردازش هست')
