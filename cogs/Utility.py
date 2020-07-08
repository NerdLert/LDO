import discord
from discord.ext import commands
from pyfiglet import Figlet

class Utility(commands.Cog):


    def __init__(self, client):
        self.client = client


    @commands.command()
    async def pyg(self, ctx, font, *, text):
        f = Figlet(font=font)
        await ctx.send(f"```{f.renderText(text)}```")
    
 
def setup(client):
    client.add_cog(Utility(client))


    