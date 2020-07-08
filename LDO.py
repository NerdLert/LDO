import discord
from discord.ext import commands
import os
import time


client = commands.Bot(command_prefix = '/')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    time.sleep(0.5)
    client.load_extension(f"cogs.{extension}")

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

for filename in os.listdir(r"C:\Users\12102\OneDrive\Desktop\LDO\cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.command()
async def servlist(ctx):
    guilds = await client.fetch_guilds(limit=150).flatten()

    await ctx.send(f"I am in these guilds: {guilds}")


client.run("NzIxNzY0OTU0MjMwNzUxMzEz.Xuee-A.6Zj_FVCl2doGFeis6ysG_vbv_TA")