import discord
import io
from PIL import Image
from discord.ext import commands
from discord import app_commands

class fun(commands.GroupCog, group_name="fun", group_description="Wow so funny"):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="image2gif", description="convert images to gifs")
    async def image2gif(self, interaction: discord.Interaction, image: discord.Attachment):
        byte = await image.read()
        gif_buffer = io.BytesIO()
        with Image.open(io.BytesIO(byte)) as img:
            img.save(gif_buffer, format="GIF")
        gif_buffer.seek(0)
        await interaction.response.send_message(file=discord.File(gif_buffer, filename="converted.gif"))
    # @app_commands.command(name="searchurban", description="Search the urban dictionary")
    # async def urban(self, interaction: discord.Interaction, search: str):
    #     word = UrbanDict(search)
    #     results = word.search()
    #     interaction.response.send_message(results[0])


async def setup(bot):
    await bot.add_cog(fun(bot))
