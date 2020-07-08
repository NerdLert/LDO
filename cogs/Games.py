import discord
from discord.ext import commands
import random


class Games(commands.Cog):


    def __init__(self, client):
        self.client = client


    @commands.command()
    async def Coinflip(self, ctx):
        possible = ['heads','tails' ]
        await ctx.send(f' I choose {random.choice(possible)}')

   



        
    









def setup(client):
    client.add_cog(Games(client))