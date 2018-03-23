import asyncio
from commands.utils.Command import Command
import requests

class List(Command):

	ftp = None

	def __init__(self):
		super().__init__(__name__.replace("commands.", ""));


	async def run(self, message, client, args, ftp):
		files = []
		files = ftp.nlst()

		file_names = ""

		for i, file_name in enumerate(files):
			file_names += file_name + (", " if (i + 1) != len(files) else "")

		await client.send_message(message.channel, "Files: "+file_names)