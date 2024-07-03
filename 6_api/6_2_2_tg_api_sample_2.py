import os
from environs import Env
import requests

env = Env()
env.read_env(os.path.join('..', '.env'))
BOT_TOKEN = env("BOT_TOKEN")
