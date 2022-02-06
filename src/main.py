
import discord

if __name__ == '__main__':

	bot			= discord.Client()
	managed_roles	= dict()

	for emoji, role in [(line.split("=")) for line in open('../config/.roles').read().splitlines()]:
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
		
		message = message.content[1:]
		# message is meant for bot, now do some stuff

		await message.channel.send('Unknown command :/')
		print('Unknown command :/')
		return

	@bot.event
	async def on_raw_reaction_add(payload):
		user	= payload.member
		message	= await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

		# the message being reacted to is not by the bot
		if message.author != bot.user:
			return

		server	= bot.get_guild(user.guild.id)
		key		= payload.emoji.name

		print(managed_roles.keys())
		print("key=",key)
		if key in managed_roles:
			print('ayooo')
			role = discord.utils.get(server.roles, name=managed_roles[key])
			await user.add_roles(role)


	@bot.event
	async def on_reaction_add_remove(reaction, user):
		# the message being reacted to is not by the bot
		if reaction.message.author != bot.user:
			return

	bot.run(open("../.token").read())
