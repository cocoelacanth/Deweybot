import discord
from discord.ext import commands, tasks
import Bot
import other.Permissions as Permissions
import gif

@Bot.tree.command(name="house", description="house dr house md car accident funny gifs")
@discord.app_commands.allowed_installs(guilds=True, users=True)
async def house(ctx : discord.Interaction, text: str):
    await ctx.response.defer(thinking=True)
        
    image_file = discord.File(gif.gen(text),filename=f"{text.replace(" ", "_")[0:32]}.gif")
    await ctx.followup.send(file=image_file)