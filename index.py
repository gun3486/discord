import discord
import asyncio
import sys

client = discord.Client()

token = sys.argv[1]
print(token)

@client.event
async def on_ready():
    print('hello')
    channel = client.get_channel(855854595585343498)
    await channel.send('test1')

client.run(token)
