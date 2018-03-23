import asyncio
from commands.utils.Command import Command

class Download(Command):

	def __init__(self):
		super().__init__(__name__.replace("commands.", ""));

	async def run(self, message, client, args, ftp):
		
		file = open(args[0], 'wb')
		ftp.retrbinary('RETR '+args[0], file.write)

		await client.send_message(message.channel, "File: ")
		await client.send_file(message.channel, args[0])