import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.ext.commands.Bot(command_prefix='$', intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ain\'t that right'):
        await message.channel.send('so true bestie')
    
    if message.author.id == "<put your best friend's id here>":
        await message.channel.send('so true {}'.format(message.author.name))

    await client.process_commands(message)

@client.command()
async def poke(ctx, *words):
    if words:
        message = ' '.join(words)
    else:
        message = '...right.'
    await ctx.send(message)
    print(f'Sent message containing: {words}')

client.run('put your bot token here heehee')
