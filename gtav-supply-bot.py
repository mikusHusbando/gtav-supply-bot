import discord
from discord.ext import commands

prefix = "?"
bot = commands.bot(command_prefox=prefix, description="A small bot keeping track of your GTA Business supplies")

@bot.event
async def on_ready():
    print('Bot is ready for use')

@bot.command()
async def setup
# register a business for timing
    return gotcha

@bot.command()
async def supplied
# add time to reminder
    return gotcha

@bot.command()
async def sold
# reset stock
    return gotcha

@bot.command()
async def pause
#pause the timer (when closing the game for example)
    return gotcha

@bot.command()
async def resume
#resume
    return gotcha

@bot.command()
async def remind
#set up a custom notification time
    return gotcha

@bot.command()
async def status
#print supply and stock info
    return gotcha
