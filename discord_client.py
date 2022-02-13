import discord

token = "OTQyNDQ4MjczMjI1MDQ0MDA4.YgkpWg.knxwVUSdK6VMnrJfYaKdbxOwouU"

client = discord.Client()

@client.event
async def on_ready():
    print('user {} is ready'.format(client))

@client.event
async def on_message(message):
    print(message)

client.run(token)
