
import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.events import newmessage
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)
from telethon import TelegramClient, events
import pyautogui

api_id = '3339307'
api_hash = '21e43ac414ea9775a83a252f47e446f2'
user_input_channel = 'https://t.me/League123bot'

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(user_input_channel))
async def my_event_handler(event):
    substring = 'Pick'
    if substring in event.raw_text:
        newText = event.raw_text.replace('Pick', "")
        pyautogui.write(newText)
        await client.disconnect()
client.start()
client.run_until_disconnected()
    


#     @client.on(events.NewMessage(chats=user_input_channel))
#     async def newMessageListener(event):
#         newMessage = event.message.message
        
