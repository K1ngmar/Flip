
import discord

async def flip_help(bot, managed_roles, message):
	# msg = f">>> {message.author.avatar_url} **| Flippy's help menu**\n"
	# msg += f"**roles:**\n"
	# for emoji, role in managed_roles.items():
	# 	msg += f"`{emoji}{role}`, "
	# msg = msg[:-2]
	# await message.channel.send(msg)

	embed=discord.Embed(
		color		= 0xff24cf
	)
	embed.set_author(name="| Flippy's help menu", icon_url=message.author.avatar_url)
	embed.add_field(name="-help", value="Shows the current help menu", inline=False)
	embed.add_field(name="-roles", value="Lists all the roles", inline=False)

	await message.channel.send(embed=embed)