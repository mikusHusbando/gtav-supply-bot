import asyncio
import time
import discord

# read token from file so it is not in the repository
with open('/root/discord-bot-secret') as f:
    discord_bot_secret = f.readline().strip()

client = discord.Client()

bot_cmd_channel = discord.Object(id='494903538753863680')

tick_amount = 100


async def check_progress_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        await wrapper("waiting 5sec")

        await asyncio.sleep(5)


async def wrapper(message_str):
    await client.send_message(bot_cmd_channel, message_str)


@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.author == client.user:
        return

    # we want to only communicate in a dedicated channel to not spam the servers. hardcoded ID for now
    if message.channel == bot_cmd_channel and message.content.startswith("!"):

        if message.content.startswith('!supplied'):
            arguments = (extractArguments(message))
            await supplied(arguments)


def extractArguments(message):
    message_parts = message.content.split(" ")
    return [message.author, message_parts[0], message_parts[1], ]


async def supplied(arguments):
    supply_time = time.time()
    resupply_time = time.time() + tick_amount*tick_seconds[arguments[1]]
    business.supplied(arguments)
    await wrapper(arguments)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(check_progress_loop())
client.run(discord_bot_secret)
