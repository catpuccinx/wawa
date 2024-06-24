import discord
import random
from discord import Intents, Client, Message
import asyncio
import os
from discord.ext import commands

# bot token
botToken = "MTI1NDY2OTk3MjM4NzM5NzcxNA.GnRqcH.nlb24c9KyXnz9GlGbkxBlXGfS4btmVX9naVj_4"

# prefix
client = commands.Bot(command_prefix=";", intents=discord.Intents.all())

# no more help
client.remove_command("help")

# status + check if online + message chat
@client.event
async def on_ready():
  game = discord.Game("with your data! ‹𝟹 ")
  await client.change_presence(status=discord.Status.idle, activity=game)
  channel = client.get_channel(1254842334554624111) 
  await channel.send("ココロ back online.")  

# cogs
async def loadCogs():
    for filename in os.listdir('./ココロ/cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await loadCogs()
        await client.start(botToken)

asyncio.run(main())


# ----------------- #
backonline = [
  "Hello, I'm online.",
  "ココロ back online.", 
  "Guess who's back, back again."
  "I still don't have a clue why I am here."
  "Logging in."
]