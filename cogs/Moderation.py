import discord
from discord.ext import commands


class moderation(commands.Cog):


    def __init__(self, client):
        self.client = client



    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):
        user = member
        await user.send(f'Kicked {member} for {reason}')
        await ctx.send(f'Kicked {member} for {reason}')
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        user = member
        await user.send(f'Banned {member} for {reason}')
        await ctx.send(f'Banned {member} for {reason}')
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *,  member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
 
        for ban_entry in banned_users:
            user = ban_entry.user
 
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator} Your Welcome.')
                return
    
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def clear(self, ctx, amount : int):
        limit = int(amount)
        await ctx.channel.purge(limit=limit)
        await ctx.send(f"Deleted {limit} Message(s)!")
        await ctx.channel.purge(limit=1)



   

def setup(client):
    client.add_cog(moderation(client))


