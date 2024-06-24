from discord.ext import commands

class aCog(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("single pings loaded!")

# a
    @commands.command()
    async def a(self, ctx):
        await ctx.send(f'{ctx.author.mention} a')

async def setup(client): 
    await client.add_cog(aCog(client))