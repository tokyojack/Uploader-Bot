from commands.utils.Command import Command

import asyncio
import requests

class Upload(Command):

	def __init__(self):
		super().__init__(__name__.replace("commands.", ""));


	async def run(self, message, client, args, ftp):
		attachments = message.attachments[0];
		proxy_url = attachments.get('url')

		f = open("temp",'wb')
		f.write(requests.get(proxy_url).content)
		f.close()

		ftp.storbinary('STOR '+attachments.get("filename"), open("temp",'rb'))

		await client.send_message(message.channel, "Uploaded")