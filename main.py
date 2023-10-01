# # https://docs.telethon.dev/en/stable/basic/signing-in.html
# # https://stackoverflow.com/questions/64155483/signing-in-to-telegram-client-with-telethon-automatically-python
# # https://github.com/LonamiWebs/Telethon
# # https://pypi.org/project/python-telegram/

# from telethon import TelegramClient, events, sync, hints
import asyncio
# from enum import Enum
# import datetime
# import json
# from json import JSONEncoder
# import time


# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 17349
api_hash = '344583e45741c457fe1862106095a5eb'



# client = TelegramClient('anon', api_id, api_hash, proxy=("socks5", '127.0.0.1', 1080))
# client.start()

# client.start()
# client.run_until_disconnected()

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

phone = '00989125305483'
username = 'my username'

# Create the client and connect
client = TelegramClient('majid', api_id, api_hash, proxy=("socks5", '127.0.0.1', 1080))
client.start()
print("Client Created")
# Ensure you're authorized
# if not client.is_user_authorized():
#     client.send_code_request(phone)
#     try:
#         client.sign_in(phone, input('Enter the code: '))
#     except SessionPasswordNeededError:
#         client.sign_in(password=input('Password: '))

async def send_mess(message):
    await client.send_message(entity='my_download', message=message)

newfeature = asyncio.run(send_mess(message="hello world"))

# with client:
    # client.send_message(entity='my_download', message="hello world")
    # await send_mess(message="hello world")
    # client.loop.run_until_complete(send_mess(message="hello world"))
