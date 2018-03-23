import discord
from discord.ext.commands import Bot
from discord.ext import commands

from ftplib import FTP

from commands.list import List
from commands.upload import Upload
from commands.download import Download


ftp = FTP(host='host')
ftp.login(user="username", passwd="password")
ftp.cwd('uploads')

Client = discord.Client();
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
	print("Mario Bot is ready!")

commands = [List(), Upload(), Download()]

@client.event
async def on_message(message):
	await client.add_reaction(message, "👍")

	message_content = message.content.lower();
	command_prefix = client.command_prefix;
	if not message_content.startswith(command_prefix):
		return;

	message_content_split = message_content.split(" ");
	args = message_content_split[1:]
	command_title = message_content_split[:1][0].replace(command_prefix, "");

	if message_content == command_prefix+"help":
		command_list = "";

		for i, command in enumerate(commands):
			command_list += command.getName() + (", " if (i + 1) != len(commands) else "")

		await client.send_message(message.channel, "Commands: "+command_list);

	else:

		for command in commands:
			if command_title == command.getName().lower():
				await command.run(message, client, args, ftp)

client.run("bot_id")