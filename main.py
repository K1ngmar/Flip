
from src.add_role import add_role
from src.help import flip_roles
from src.help import flip_help
from src.help import flip_verysecretpincommand
import discord

if __name__ == '__main__':

	bot				= discord.Client()
	managed_roles	= dict()

	for emoji, role in [(line.split("=")) for line in open('./config/.roles').read().splitlines()]:
		managed_roles[emoji] = role

	@bot.event
	async def on_ready():
		print(bot.user)

	@bot.event
	async def on_message(message):
		# message by the bot itself
		if message.author == bot.user:
			return

		# message not meant for bot
		if message.content.startswith('-') == False:
			return
		
		command = message.content[1:]
		# message is meant for bot, now do some stuff
		if command == "help":
			await flip_help(bot, managed_roles, message)
		elif command == "roles":
			await flip_roles(bot, managed_roles, message)
		elif command == "verysecretpincommand:
			await flip_verysecretpincommand(bot, managed_roles, message)
		else:
			await message.channel.send('Unknown command :/')
		return

	@bot.event
	async def on_raw_reaction_add(payload):
		await add_role(bot, payload, managed_roles)

	@bot.event
	async def on_reaction_add_remove(reaction, user):
		# the message being reacted to is not by the bot
		if reaction.message.author != bot.user:
			return

	bot.run(open("./.token").read())
