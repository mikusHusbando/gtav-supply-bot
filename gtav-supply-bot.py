# -*- coding: utf-8 -*-
import asyncio
import time

import discord

from classes.business import business
from classes.timerdata import timerData

# read token from file so it is not in the repository
with open('/root/discord-bot-secret') as f:
    discord_bot_secret = f.readline().strip()

client = discord.Client()
business_object = business()
timer_data_object = timerData()
bot_cmd_channel = discord.Object(id='494903538753863680')

tick_amount = 100


async def check_progress_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        # await message_wrapper('waiting 5sec')
        for elapsed_timer in timer_data_object.get_elapsed_timer():  # message that timer ended for the given type and author. does nothing if no timer elapsed
            await message_wrapper(
                'timer for {} is up for author id {}!'.format(elapsed_timer['type'], elapsed_timer['author_id']))
        await asyncio.sleep(5)


async def message_wrapper(message_str):
    await client.send_message(bot_cmd_channel, message_str)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # we want to only communicate in a dedicated channel to not spam the servers. hardcoded ID for now
    # if message.channel == bot_cmd_channel and message.content.startswith('!'):
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!supplied'):
        await supplied(extract_arguments(message))


def extract_arguments(message):
    out = [message.author.id]
    for c in message.content.split(' '):
        out.append(c)
    return out


async def supplied(arguments):
    business_details = business_object.get_business_details(arguments[2])

    if business_details is not None:
        resupply_time = time.time() + tick_amount * business_details
        timer_data_object.add_timer(arguments[0], business_details, resupply_time)
        # out_message = 'added timer for {} running {} seconds!'.format(business_details, resupply_time)
        await message_wrapper("success")
        return None
    await message_wrapper("fail")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(check_progress_loop())
client.run(discord_bot_secret)
