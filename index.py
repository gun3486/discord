from asyncio.tasks import sleep
import discord
import asyncio
import sys
import threading, time
import schedule
import datetime

client = discord.Client()

token = sys.argv[1]
print(token)

async def loop():
    time.sleep(3)
    while True:
        channel = client.get_channel(855854595585343498)
        await channel.send("지금은 유리시입니다.")
        time.sleep(1)

async def callback():
    await loop()

def between_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.
    loop.run_until_complete(callback())
    loop.close()

thread = threading.Thread(target=between_callback)
thread.start()

client.run(token)