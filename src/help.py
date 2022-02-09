
import discord

async def flip_help(bot, managed_roles, message):
	embed=discord.Embed(
		color		= 0xff24cf
	)
	embed.set_author(name=" Flippy's help menu", icon_url=message.author.avatar_url)
	embed.add_field(name="-help", value="Shows the current help menu", inline=False)
	embed.add_field(name="-roles", value="Lists all the roles", inline=False)

	await message.channel.send(embed=embed)
	return

# returns a format string with all the managed roles and their emojis
def get_managed_roles(managed_roles):
	msg = f""
	for emoji, role in managed_roles.items():
		msg += f"`{emoji}{role}`,\n"
	msg = msg[:-2]
	return msg

async def flip_roles(bot, managed_roles, message):
	embed=discord.Embed(
		color		= 0xff24cf
	)
	embed.set_author(name=" Flippy's role manager", icon_url=message.author.avatar_url)
	embed.add_field(name="managed roles:", value=get_managed_roles(managed_roles), inline=False)
	embed.add_field(
		name="about:",
		value="You can gain roles by reacting to flip's pinned message with the corresponding emoji in the flip channel!"
	)

	await message.channel.send(embed=embed)
	return