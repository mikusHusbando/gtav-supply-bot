import discord
from discord.ext import commands

prefix = "?"
bot = commands.bot(command_prefox=prefix, description="A small bot keeping track of your GTA Business supplies")

@bot.event
async def on_ready():
    print('Bot is ready for use')

@bot.command
async def track
# register a business for tracking

@bot.command()
async def setup
# fills the supplies of a business (done as part of the setup mission
    return gotcha

@bot.command()
async def supplied
# sets the supply to full in 10 minutes
    return gotcha

@bot.command()
async def sold
# reset stock to zero
    return gotcha

@bot.command()
async def raided
# reset stock to zero
# reset supplies to zero
#
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
