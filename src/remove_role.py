
import discord
from discord.utils import get

async def remove_role(bot, payload, managed_roles):
	server = await bot.fetch_guild(payload.guild_id)
	user = await server.fetch_member(payload.user_id)
	message	= await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

	# the message being reacted to is not by the bot
	if message.author != bot.user:
		return

	# Its not a pinned message
	if message.pinned == False:
		return

	if user == bot.user:
		return

	key	= payload.emoji.name

	if key in managed_roles:
		print(f"removed role {key}{managed_roles[key]} from user '{user}'")
		role = discord.utils.get(server.roles, name=managed_roles[key])
		await user.remove_roles(role)
	return
