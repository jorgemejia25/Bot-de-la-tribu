import discord
from discord.ext import commands

client = discord.Client()
@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("Power"):
        await message.channel.send("Chinga a tu madre @Power")
    if message.content.startswith("Fercho"):
        await message.channel.send("Me vengo")
    if message.content.startswith("wolf"):
        await message.channel.send("cara culo")
    if message.content.startswith("Pasa ip"):
        await message.channel.send("No pinche puta")
    if message.content.startswith("lorito"):
        await message.channel.send("Pajaro generico chillon")
        await message.channel.send("pajaro qliao maricon y generico")
    if message.content.startswith(".nahu"):
        await message.channel.send("re gei")
    if message.content.startswith("crema"):
        await message.channel.send("Re gei")
    if message.content.startswith("J3B"):
        await message.channel.send("-p caballo homosexual de las montañas")
    if message.content.startswith("gato"):
        await message.channel.send("michi gay")
    if message.content.startswith("Kenny lee"):
        await message.channel.send("Ohhhh me vengo")
    if message.content.startswith("Gilbert"):
        await message.channel.send("Soy añañin")
client.run('NzQ2OTUwMjk4MDE0MzE4NjE3.X0HxrA.3OVyEUdcbObVwFsfBXWYTdylgPg')
