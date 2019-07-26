import discord
import sys
from discord.ext import commands

TOKEN = open("token","r").readline().strip()

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
	print('Logged in as ' + client.user.name)
	#for x in client.get_all_channels():
	#	await x.send('pi now available')

@client.event
async def on_message(message):
	if(message.author != client.user):
		await message.channel.send('Got ' + message.content + ' from ' + message.author.mention)

client.run(TOKEN)

