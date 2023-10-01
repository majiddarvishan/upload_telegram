# https://docs.telethon.dev/en/stable/modules/client.html#telethon.client.messages.MessageMethods.send_message
# https://stackoverflow.com/questions/76383605/how-do-i-upload-large-files-to-telegram-in-python
# https://github.com/MiyukiKun/FastTelethonhelper/blob/main/README.md

from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from telethon.errors import SessionPasswordNeededError
import socks
import socket
from pytube import YouTube



#########################

proxy_host = '127.0.0.1'
proxy_port = 1080

# Set the SOCKS proxy for pytube
socks.set_default_proxy(socks.SOCKS5, proxy_host, proxy_port)
socket.socket = socks.socksocket

def progress_callback(stream, chunk, bytes_remaining) -> None:
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"{percentage_of_completion:.2f}% downloaded")

def download_video(url: str) -> None:
    print(url)
    yt = YouTube(url, on_progress_callback=progress_callback)
    print(yt.title)

    # video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    # print(video.resolution)
    # video = yt.streams.filter(file_extension='mp4').get_by_resolution('360p').download()

with open('urls.txt') as f:
    for line in f:
        download_video(line.rstrip())


#########################


# # get your api_id, api_hash, token
# # from telegram as described above
# api_id = 17349
# api_hash = '344583e45741c457fe1862106095a5eb'
# token = 'bot token'
# message = "Working..."

# # your phone number
# phone = '00989125305483'

# # creating a telegram session and assigning
# # it to a variable client
# client = TelegramClient('anon', api_id, api_hash, proxy=("socks5", proxy_host, proxy_port))

# # connecting and building the session
# client.connect()

# # in case of script ran first time it will
# # ask either to input token or otp sent to
# # number or sent or your telegram id
# if not client.is_user_authorized():
#     client.send_code_request(phone)

#     try:
#         client.sign_in(phone, input('Enter the code: '))
#     except SessionPasswordNeededError:
#         client.sign_in(password=input('Password: '))

# try:
#     # receiver user_id and access_hash, use
#     # my user_id and access_hash for reference
#     receiver = InputPeerUser('user_id', 'user_hash')

#     # sending message using telegram client
#     # client.send_message(receiver, message, parse_mode='html')
#     # client.send_message("me", message=message)
#     client.send_file("me", './log.txt', caption="Test video")
# except Exception as e:

#     # there may be many error coming in while like peer
#     # error, wrong access_hash, flood_error, etc
#     print(e)

# # disconnecting the telegram session
# client.disconnect()
