import discord
from discord.ext import commands

class tag(commands.Cog): 

    @commands.Cog.listener()
    async def on_ready(self):
        print("everyone ping loaded!")

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def bday(self, ctx):
        await ctx.send("{ctx.author.mention}'s birthday! @everyone")

    @commands.command()
    async def christmas(self, ctx):
        await ctx.send("Happy Christmas @everyone")

async def setup(client): 
    await client.add_cog(tag(client))