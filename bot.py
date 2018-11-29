import discord 
from discord.ext.commands import Bot
from discord.ext import commands 
from discord.ext.commands.cooldowns import BucketType 
import asyncio 
import platform
import colorsys
import random
import os
import time
 
import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='f!')

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	
@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def kick(ctx,user:discord.Member):

    if user.server_permissions.kick_members:
        await bot.say('**Nemáš Oprávnění na kick a nebo je dotyčný Administrátor**')
        return
    
    try:
        await bot.kick(user)
        await bot.say(user.name+' byl kicknut. Měj se '+user.name+'!')
        await bot.delete_message(ctx.message)

    except discord.Forbidden:
        await bot.say('Permission denied.')
        return	
	

bot.run(os.getenv("BOT_TOKEN"))

