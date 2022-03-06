
import discord

# displays help menu when -help is called
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

# displays the roles when -roles is called
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

# The pinned message people will be able to react to
async def flip_verysecretpincommand(bot, managed_roles, message):
	embed=discord.Embed(
		color		= 0xff24cf
	)
	embed.set_author(name=" Flippy's assignation module", icon_url=message.author.avatar_url)
	embed.add_field(name="Roles:", value=get_managed_roles(managed_roles), inline=False)
	embed.add_field(
		name="Choose wisely......",
		value="By responding to this message with one of the emoji's above, you will be granted that role, removing your reaction will also take away the role. May the Flip be with you (╯°□°)╯︵ ┻━┻"
	)

	post = await message.channel.send(embed=embed)
	await post.pin()
	for emoji in managed_roles.keys():
		await post.add_reaction(emoji)
	return
