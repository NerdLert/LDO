import discord
from discord.ext import commands
from pyfiglet import Figlet

class Utility(commands.Cog):


    def __init__(self, client):
        self.client = client



def setup(client):
    client.add_cog(Utility(client))
