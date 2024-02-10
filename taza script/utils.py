import datetime
from telebot import types
from Conf import *
# from googleapiclient.discovery import build
# from google.oauth2 import service_account
#

class ActiveDrives:
    def __init__(self, email, service_account_file_path, parent_folder_id, free_space):
        self.email = email
        self.service_account_file_path = service_account_file_path
        self.parent_folder_id = parent_folder_id
        self.free_space = free_space


class Time:
    def __init__(self):
        self.start_time = datetime.datetime.now()

    def has_passed(self, minute):
        current_time = datetime.datetime.now()
        time_difference = current_time - self.start_time
        return time_difference.total_seconds() > (minute * 60)


class File:
    def __init__(self, Gd_id, drive:ActiveDrives, Tl_id, size):
        self.drive = drive
        self.Gd_id = Gd_id
        self.Tl_id = Tl_id
        self.size = size
        self.time = Time


class Request:
    def __init__(self, method, message=None, file: File = None):
        self.method = method
        self.message = message
        self.file = file


class Keyboard(types.ReplyKeyboardMarkup):
    def __init__(self, commands, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for command in commands:
            button = types.KeyboardButton(command)
            self.add(button)


def check_available_drive(file_size):
    for drive in active_Drives:
        if drive.free_space - (file_size / (1024 ** 2)) > 100:
            return drive

    return False


def was_it_linked(filesList, id):
    for file in filesList:
        if file.Tl_id == id:
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


def check_user_requests(chat_id, user_requests: dict, bot):
    request_count = user_requests.get(chat_id, 0)

    max_requests = 3

    if request_count >= max_requests:
        bot.send_message(chat_id, 'در هر 5 دق مجاز به فرستادن 3 فایل هستید !!!')
        return False

    else:
        user_requests[chat_id] = request_count + 1
        return True


def reset_user_requests(user_requests:dict):
    user_requests.clear()


#####################################################
# Google Drive

#
# def API_authenticate(service_account_file_path):
#     creds = service_account.Credentials.from_service_account_file(service_account_file_path, scopes=SCOPES)
#     return creds
#
#
# def get_url(file_id):
#     return f'https://drive.google.com/uc?export=download&amp;confirm=ABCD&amp;id={file_id}'
#
#
# def file_duplicate_check(service, file_metadata, parent_folder_id):
#
#     # Check if a file with the same name exists in the parent folder
#     query = f"'{parent_folder_id}' in parents and name = '{file_metadata['name']}' and trashed = false"
#     response = service.files().list(q=query, fields='files(id)').execute()
#     files = response.get('files', [])
#
#     if files:
#         # File with the same name already exists
#         # Append a unique identifier to the file name
#         file_metadata['name'] = f"{file_metadata['name']}_{len(files)}"
#
#     return file_metadata
#
#
# def Gdupload(file_path, file_name, creds, parent_folder_id):
#     service = build('drive', 'v3', credentials=creds)
#
#     file_metadata = {
#         'name': f'{file_name}',
#         'parents': [parent_folder_id],
#     }
#
#     file_metadata = file_duplicate_check(service, file_metadata, parent_folder_id)
#
#     file = service.files().create(
#         body=file_metadata,
#         media_body=file_path
#     ).execute()
#
#     # Get file id
#     results = service.files().list(
#         q=f"name='{file_name}'",
#         fields="files(id)"
#     ).execute()
#
#     files = results.get('files', [])
#
#     return files[0]['id']
#
#
# def GdPublic(file_id, creds):
#     service = build('drive', 'v3', credentials=creds)
#
#     permission = service.permissions().create(
#         fileId=file_id,
#         body={"role": "reader", "type": "anyone"}
#     ).execute()
#
#
# def GdDelete_file(file_id, creds):
#     service = build('drive', 'v3', credentials=creds)
#
#     service.files().delete(fileId=file_id).execute()
#
#
