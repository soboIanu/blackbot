token = "MzQ4MTMxNzczODYwOTM3NzI4.DHjBdA.YfFrbDKGqEZLF3Zk0mNaIOCgvk8"

import discord
import asyncio
import logging
import json
from urllib.parse import urlparse

client = discord.Client()
logging.basicConfig(level=logging.INFO)
name = "blackbot"
ver = "0.1"

@client.event
async def on_ready():
    print(name + "_" + ver)

@client.event
async def on_message(message):
    msg_splitspaces = message.content.split(" ")
    for msgpart in msg_splitspaces:
            parsecheck = urlparse(msgpart)
            if parsecheck.scheme:
                json = {message.channel.name:message.content}
                with open("userslinks.json", "a+") as jsonfile:
                    jsonfile.write("\n" + str(json))
                await client.send_message(message.channel, "Got it.")
                myvar = json.load(jsonfile)
                print(len(myvar))

client.run(token)
