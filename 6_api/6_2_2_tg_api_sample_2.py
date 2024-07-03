import os
from environs import Env
import requests

env = Env()
env.read_env(os.path.join('..', '.env'))
BOT_TOKEN = env('BOT_TOKEN')
API_URL = 'https://api.telegram.org/bot'
TEXT = "Update"

updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates').json()
#updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
if updates['result']:
    for res in updates['result']:
        print(res)


#{'update_id': 763334319, 'message': {'message_id': 78, 'from': {'id': 903775208, 'is_bot': False, 'first_name': 'Alex', 'last_name': 'V', 'username': 'Henri_Fleury', 'language_code': 'en'}, 'chat': {'id': 903775208, 'first_name': 'Alex', 'last_name': 'V', 'username': 'Henri_Fleury', 'type': 'private'}, 'date': 1719988743, 'text': '1'}}
