import discord

token = ""

client = discord.Client()

@client.event
async def on_ready():
    print('user {} is ready'.format(client))

@client.event
async def on_message(message):
    print(message)

client.run(token)
