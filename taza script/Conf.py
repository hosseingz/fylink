from utils import ActiveDrives

SCOPES = ['https://www.googleapis.com/auth/drive']
TOKEN = "6965439713:AAGI-U0XQH29qwZNmmFN1Xo-mDZ0L38wCeU"

active_Drives = [
    ActiveDrives(
        email='odugrbtt@gmail.com',
        service_account_file_path='media/service account files/hossein.gasemzade3.json',
        parent_folder_id='1KPVSg9Bbiu2y1qK4apsy7rcX02SUs6Ly',
        free_space=14000
    ),

    ActiveDrives(
        email='hossein.gasemzadeh3@gmail.com',
        service_account_file_path='media/service account files/odugrbtt.json',
        parent_folder_id='1wTgZpcNdm-CyGOE_5Ovg8Q6NnQlz9ko7',
        free_space=14000
    ),
]
