import discord
import sys

# read token from file so it is not in the repository
with open('/root/discord-bot-secret') as f:
    discord_bot_secret = f.readline().strip()

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(discord_bot_secret)

@client.event
async def on_ready():
    print('Bot is ready for use')

@client.event
async def track(business):
    client.send_message(message.channel, "tracking" + business)
    return

@client.event()
async def setup(business):
    # fills the supplies of a business (done as part of the setup mission
    return

@client.event()
async def supplied(business):
    # sets the supply to full in 10 minutes
    return

@client.event()
async def sold(business):
    # reset stock to zero
    return

@client.event()
async def raided(business):
    # reset stock to zero
    # ask about supplies, gangster or police raid?
    # maybe call this reset and let the user choose
    return

@client.event()
async def pause(business):
    # pause the timer (when closing the game for example)
    # maybe automatically call this if we pick up user leaving gta
    return

@client.event()
async def resume(business):
    #resume
    return

@client.event()
async def remind(minutes):
    # set up a custom notification time
    return

@client.event()
async def status():
    # print supply and stock info
    return
