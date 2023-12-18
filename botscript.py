from telethon.sync import TelegramClient,events
from datetime import datetime, timedelta
from time import time
import os, requests

api_id = ""
api_hash = ""



channels_list = ["-1001997205550"]
out_channel = -1002065765694

if not api_id:
    api_id = input("enter the api_id: ")
if not api_hash:
    api_hash = input("enter the api_hash: ")


client = TelegramClient('bot', int(api_id), api_hash)

client.start()


def get_entities():
    entity_list= []
    for channel in channels_list:
        try:
            input_par = int(channel)
        except:
            input_par = channel
        entity=client.get_input_entity(input_par)
        entity_list.append(entity)
    return entity_list

entities = get_entities()

@client.on(events.NewMessage(entities,incoming=True))
async def handler(message):
    if message.text:
        if message.text.startswith('/'):
            return
        try:
            if message.media:
                if hasattr(message.media,'webpage'):
                    out_channel= await client.get_input_entity(out_channel)
                    await client.send_message(out_channel,message.text)
                else:
                    out_channel = await client.get_input_entity(out_channel)
                    await client.send_file(out_channel,message.media,caption=message.text)
            else:
                out_channel= await client.get_input_entity(out_channel)
                await client.send_message(out_channel,message.text)
        except Exception as e:
            print(e)
            print(type(e).__name__)
        else:
            print('A msg with text forwarded succesfully')
    elif message.media:
        try:
            if not (hasattr(message.media,'webpage')):
                out_channel = await client.get_input_entity(out_channel)
                await client.send_file(out_channel,message.media)
        except Exception as e:
            print(e)
            print(type(e).__name__)


print('\nBot is started and will try to forward all rcvd msgs from source group to destination group, please make sure to leave this window open(do not close it)\n')

client.run_until_disconnected()