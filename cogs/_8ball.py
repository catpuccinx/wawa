import discord
import random
from discord.ext import commands

class Ball(commands.Cog): 

    @commands.Cog.listener()
    async def on_ready(self):
        print("8ball loaded!")

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, question ):
        responses = [
        "È certo.",
        "È decisamente così.",
        "Senza dubbio.",
        "Sì, sicuramente.",
        "Ci può fare affidamento.",
        "Per come la vedo io, sì.",
        "Molto probabilmente.",
        "Prospettiva positiva.",
        "Sì.",
        "Gli indizi portano a un sì.",
        "Risposta confusa, riprova.",
        "Chiedi di nuovo più tardi.",
        "Meglio non dirtelo ora.",
        "Non posso fare previsioni ora.",
        "Concentrati e chiedi di nuovo.",
        "Non ci contare.",
        "La mia risposta è no.",
        "Le mie fonti dicono di no.",
        "Le prospettive non sono buone.",
        "No.",
        "Molto dubbioso."
    ]
        await ctx.send(f"Domanda: {question}\nRisposta: {random.choice(responses)}")
    
async def setup(client): 
    await client.add_cog(Ball(client))