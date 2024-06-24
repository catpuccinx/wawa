from discord.ext import commands

class testCog(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("test loaded!")

# test
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"my ping is {round(self.client.latency * 1000)}ms")

async def setup(client): 
    await client.add_cog(testCog(client))