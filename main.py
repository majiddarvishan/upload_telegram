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
import os
import yt_dlp
import json

socks_proxy=("socks5", '127.0.0.1', 1080)
socks_proxy= None
# Set the SOCKS proxy for pytube
# socks.set_default_proxy(socks.SOCKS5, proxy_host, proxy_port)
# socket.socket = socks.socksocket

############ telegram #############

# # from telegram as described above
api_id = 17349
api_hash = '344583e45741c457fe1862106095a5eb'

# creating a telegram session and assigning
# it to a variable client
tel_client = TelegramClient('anon', api_id, api_hash, proxy=socks_proxy)

# connecting and building the session
tel_client.connect()

# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
if not tel_client.is_user_authorized():
    phone = input('Enter the phone: ')
    tel_client.send_code_request(phone)

    try:
        tel_client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        tel_client.sign_in(password=input('Password: '))


def upload_file(filename : str, title : str):
    try:
        # receiver user_id and access_hash, use
        # my user_id and access_hash for reference
        # receiver = InputPeerUser('user_id', 'user_hash')

        # sending message using telegram client
        # tel_client.send_message(receiver, message, parse_mode='html')
        # tel_client.send_message("me", message=message)
        tel_client.send_file("me", filename, caption=title)
    except Exception as e:
        # there may be many error coming in while like peer
        # error, wrong access_hash, flood_error, etc
        print(e)

############ youtube #############

def progress_callback(stream, chunk, bytes_remaining) -> None:
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"{percentage_of_completion:.2f}% downloaded")

def download_video(url: str) -> None:
    yt = YouTube(url, on_progress_callback=progress_callback)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    # print(video.resolution)
    # video = yt.streams.filter(file_extension='mp4').get_by_resolution('360p').download()

    return str(video), yt.title

def download_video_2(url, cookies_file):
    video_file = "test.mp4"
    video_title = ""
    ydl_opts = {
        'format': 'best',
        #'outtmpl': '%(title)s.%(ext)s',
        'outtmpl': 'test.mp4',
        'cookiefile': cookies_file,
        'quiet': True,  # Suppress output
        'print': 'filename',  # Print the filename after download
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_title = (info['title'])
        #video_file = f"{info['title']}.{info['ext']}"
        #video_title = ydl.sanitize_info(info)
        #print(video_title)
        #print(json.dumps(ydl.sanitize_info(info)))
        result = ydl.download([url])
        #if result:
        print(f"Downloaded file: {result}")
    return video_file, video_title

with open('urls.txt') as f:
    for line in f:
        if len(line) == 0:
            continue
        if line[0] == '#':
            tel_client.send_message("me", message=line)
            continue
        if "youtube.com" in line:
            #video_file, video_title = download_video(line.rstrip())
            video_file, video_title = download_video_2(line.rstrip(), "./cookies.txt")
            upload_file(video_file, video_title)
            os.remove(video_file)


# disconnecting the telegram session
tel_client.disconnect()
