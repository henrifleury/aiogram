import os
from environs import Env

import requests
import time

env = Env()
env.read_env(os.path.join('..', '.env'))

BOT_TOKEN = env('BOT_TOKEN')
API_URL = 'https://api.telegram.org/bot'
TEXT = 'Update'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    print(f'attempt {counter}')
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/get_Updates?offset={offset + 1}').json()
    if updates['result']:
        for res in updates['result']:
            offset = res['update_id']
            chat_id = res['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT} cur_offset {offset}')

