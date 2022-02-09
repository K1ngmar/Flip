import discord

async def add_role(bot, payload, managed_roles):
	user	= payload.member
	message	= await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

	# the message being reacted to is not by the bot
	if message.author != bot.user:
		return

	# Its not a pinned message
	if message.pinned == False:
		return

	server	= bot.get_guild(user.guild.id)
	key		= payload.emoji.name

	if key in managed_roles:
		print(f"added role {key}{managed_roles[key]} to user '{user.name}'")
		role = discord.utils.get(server.roles, name=managed_roles[key])
		await user.add_roles(role)
	return
