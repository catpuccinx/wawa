
# -------------------------------------- #
import discord
from discord.ext import commands

class Nudge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("help.py is online.")

    @commands.command()
    async def poke(self, ctx):
        poke = discord.Embed(title="What happened!?", description="Gasp, you've been poked!", color=0xffb7b7)

        poke.set_image(url="https://files.catbox.moe/7jze5h.gif")
        poke.set_footer(text=f"Requested by {ctx.author.mention}.", icon_url=ctx.author.avatar)

        await ctx.send(embed=poke)

async def setup(client):
    await client.add_cog(Nudge(client))