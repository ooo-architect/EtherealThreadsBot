import logging
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.environ['TOKEN']
CHAT_ID = int(os.environ['CHAT_ID'])
CHANNEL_ID = int(os.environ['CHANNEL_ID'])

print(f'{TOKEN=}\n{CHAT_ID=}\n{CHANNEL_ID=}')