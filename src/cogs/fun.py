import discord
import io
from PIL import Image
from discord.ext import commands
from discord import app_commands

#Create a group and cog for fun commands
class fun(commands.GroupCog, group_name="fun", group_description="Wow so funny"):
    def __init__(self, bot):
        self.bot = bot
    
    #Image to gif conversion
    @app_commands.command(name="image2gif", description="convert images to gifs")
    async def image2gif(self, interaction: discord.Interaction, image: discord.Attachment):
        await interaction.response.defer()
        #Save the gif to a RAM buffer
        byte = await image.read()
        gif_buffer = io.BytesIO()
        with Image.open(io.BytesIO(byte)) as img:
            img.save(gif_buffer, format="GIF")
        #Send the image from the gif buffer
        gif_buffer.seek(0)
        await interaction.followup.send(file=discord.File(gif_buffer, filename="converted.gif"))
        print("converted an image to a gif")
    # @app_commands.command(name="searchurban", description="Search the urban dictionary")
    # async def urban(self, interaction: discord.Interaction, search: str):
    #     word = UrbanDict(search)
    #     results = word.search()
    #     interaction.response.send_message(results[0])


async def setup(bot):
    await bot.add_cog(fun(bot))
