import discord
client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="Making a    bot"))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await message.channel.send("World")
client.run('NjA4ODA0OTQ1MjYwNDQ1Njk5.XUv_eA.teMBn3LtERMjgMtiCTQC1kHd4mU')