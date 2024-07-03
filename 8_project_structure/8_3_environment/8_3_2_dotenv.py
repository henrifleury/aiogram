# https://stepik.org/lesson/759402/step/3?unit=761418
# to get ADMIN_ID - https://t.me/getmyid_bot
# or parse bot updates

import os
# pip3 install python-dotenv
import dotenv
dotenv.load_dotenv("../../.env")
print(os.getenv('BOT_TOKEN'))
print(os.getenv('ADMIN_ID'))
