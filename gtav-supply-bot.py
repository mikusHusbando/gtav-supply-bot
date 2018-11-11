import time

import discord

# read token from file so it is not in the repository
with open('/root/discord-bot-secret') as f:
    discord_bot_secret = f.readline().strip()

client = discord.Client()

business = [{'type': 'bunker', 'ticTime': 84}, {'type': 'coke', 'ticTime': 72}, {'type': 'meth', 'ticTime': 90},
            {'type': 'cash', 'ticTime': 96}, {'type': 'weed', 'ticTime': 120}, {'type': 'docs', 'ticTime': 90}]

bot_cmd_channel = discord.Object(id='494903538753863680')

amountTicks = 100


async def check_progress_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        #for b in business:
        #    if b.type == parameter:
        #        threading.Timer(time.time() + (ticSum * b.ticTime), timeIsUp, [message, parameter])
        #        await client.send_message(message.channel,
        #                                  'started timer for {}, finishes : {}.'.format(parameter,
        #                                                                                timer[business.index(parameter)]))
        await wrapper("waiting 5sec")
        await asyncio.sleep(5)



async def wrapper(message_str):
    await client.send_message(bot_cmd_channel, message_str)

    @client.event
    async def on_message(message):

        # we want to only communicate in a dedicated channel to not spam the servers. hardcoded ID for now
        if message.channel == bot_cmd_channel:

            if message.author == client.user:
                return

            if message.content.startswith('!supplied'):
                arguments = (extractArguments(message))
                await supplied(arguments)

            if message.content.startswith('!hello'):
                msg = 'Hello {0.author.mention}'.format(message)
                await client.send_message(message.channel, msg)

    def extractArguments(message):
        message_parts = message.content.split(" ")
        return [message.author, message_parts[0], message_parts[1], ]

    async def supplied(arguments):
        await wrapper(arguments)

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    client.loop.create_task(check_progress_loop())

    client.run(discord_bot_secret)
