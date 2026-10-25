import discord
from discord.ext import commands
from discord import app_commands

class fun(commands.GroupCog, group_name="fun", group_description="Wow so funny"):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="image2gif")
    async def image2gif(self, interaction: discord.Interaction, image: discord.Attachment):
        await interaction.response.send_message(image)

async def setup(bot):
    await bot.add_cog(fun(bot))
