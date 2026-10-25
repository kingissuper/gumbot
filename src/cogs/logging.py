import discord
from discord.ext import commands
from datetime import datetime

class messageLogging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #helper function for embeds
    @classmethod
    def format_embed(self, title: str, colour: cls, user_id: str, user: str):
        embed = discord.Embed(timestamp=datetime.now(), colour=colour, title=title, description=f"By '{user}'<@{user_id}>")
        return embed

    @commands.Cog.listener()
    async def on_raw_message_edit(self, RawMessageUpdateEvent):
        removed_attachments = []
        after = RawMessageUpdateEvent.message
        if after.author.bot:
            return
        if RawMessageUpdateEvent.cached_message:
            before = RawMessageUpdateEvent.cached_message
            before_value = before.content
            for attachment in before.attachments:
                if attachment not in after.attachments:
                    removed_attachments.append(attachment.url)
        else:
            before_value = "Unknown"
        if removed_attachments != []:
            embed = self.format_embed(colour=discord.Colour.dark_red(), title="Attachment deleted", user_id=after.author.id, user=after.author.global_name)
            embed.add_field(name="Removed attachments:", value=removed_attachments, inline=False)
            await after.channel.send(embed=embed)
            return
        embed = self.format_embed(colour=discord.Colour.orange(), title="Message edited", user_id=after.author.id, user=after.author.global_name)
        embed.add_field(name="Before", value=before_value)
        embed.add_field(name="After", value=after.content)
        await after.channel.send(embed=embed)
        

    @commands.Cog.listener()
    #TODO: rewrite for on_raw_message_delete
    async def on_message_delete(self, message: discord.Message):
        if message.author.bot:
            return
        embed = self.format_embed(colour=discord.Colour.dark_red(), title="Message deleted", user_id=message.author.id, user=message.author.global_name)
        embed.add_field(name="Message", value=message.content)
        await message.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(messageLogging(bot))