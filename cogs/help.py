import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("help.py is online.")

    @commands.command()
    async def help(self, ctx):
        help_embed = discord.Embed(title="Need help?", description="A list of aviable commands.", color=0xffb7b7)

        help_embed.add_field(name=";help", value="Shows this message.", inline=False)
        help_embed.add_field(name=";8ball", value="Just like the magic ball, answer yes and no questions.", inline=False)
        help_embed.add_field(name=";consiglio", value="Gives you advices from the tarots.", inline=False)
        help_embed.add_field(name=";ping", value="Shows the bot's ping", inline=False)
        help_embed.add_field(name=";poke", value="Poke everyone!", inline=False)
        help_embed.set_footer(text=f"Requested by <@{ctx.author}>.", icon_url=ctx.author.avatar)

        await ctx.send(embed=help_embed)

async def setup(client):
    await client.add_cog(Help(client))