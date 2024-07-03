#pip3 install environs
import os
from environs import Env
env = Env()

#local .env
env.read_env()
tmp_env_var = env("TMP_ENV")
print(tmp_env_var, type(tmp_env_var))

env = Env()
# .env from another directory
env.read_env("../../.env")

bot_token = env('BOT_TOKEN')
admin_id = env.int('ADMIN_ID')

print(bot_token)
print(admin_id)

print(os.getenv('BOT_TOKEN'))
print(os.getenv('ADMIN_ID'))