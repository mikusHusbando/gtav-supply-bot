import discord

#read token from file so it is not in the repository
with open('~/discord-bot-secret') as f:
    discord_bot_secret = f.readline().strip()

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        client.send_message(message.channel, msg)

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

@client.command
async def track(business):
# register a business for tracking

@client.command()
async def setup(business):
# fills the supplies of a business (done as part of the setup mission
    return

@client.command()
async def supplied(business):
# sets the supply to full in 10 minutes
    return

@client.command()
async def sold(business):
# reset stock to zero
    return

@client.command()
async def raided(business):
# reset stock to zero
#ask about supplies, gangster or police raid?
#maybe call this reset and let the user choose

@client.command()
async def pause(business):
#pause the timer (when closing the game for example)
#maybe automatically call this if we pick up user leaving gta
    return

@client.command()
async def resume(business):
#resume
    return

@client.command()
async def remind(minutes):
#set up a custom notification time
    return

@client.command()
async def status():
#print supply and stock info
    return
