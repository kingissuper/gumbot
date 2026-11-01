import discord
from discord.ext import commands
from datetime import datetime

#Create a group and cog for logging
class messageLogging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #helper function for embeds
    @classmethod
    def format_embed(self, title: str, colour: cls, author: discord.Message.author|None, message_id: int):
        embed = discord.Embed(timestamp=datetime.now(), colour=colour, title=title, description=f"By '{author.global_name}'<@{author.id}>")
        embed.set_footer(text=f"Author ID; {author.id if author else "Unknown"}, Message ID; {message_id}")
        return embed

    #Listener for edited messages
    @commands.Cog.listener()
    async def on_raw_message_edit(self, RawMessageUpdateEvent):
        removed_attachments = []
        after = RawMessageUpdateEvent.message
        #Cancel if the message originated from a bot
        #TODO remove when database added
        if after.author.bot:
            return
        #Check if the previous message content is cached
        if RawMessageUpdateEvent.cached_message:
            before = RawMessageUpdateEvent.cached_message
            before_value = before.content
            #Check for attachment changes
            for attachment in before.attachments:
                if attachment not in after.attachments:
                    removed_attachments.append(attachment.url)
        #If the previous message content isn't cached(usually after bot restart)
        else:
            before_value = "Unknown"
        #Send the embed for attachment changes if there was one
        if removed_attachments != []:
            embed = self.format_embed(colour=discord.Colour.dark_red(), title="Attachment deleted", author=after.author, message_id=RawMessageUpdateEvent.message_id)
            embed.add_field(name="Removed attachments:", value=removed_attachments, inline=False)
            await after.channel.send(embed=embed)
            return
        #Otherwise send the message changes
        embed = self.format_embed(colour=discord.Colour.orange(), title="Message edited", author=after.author, message_id=RawMessageUpdateEvent.message_id)
        embed.add_field(name="Before", value=before_value)
        embed.add_field(name="After", value=after.content)
        await after.channel.send(embed=embed)
        print(f"message was edited in {RawMessageUpdateEvent.channel_id}")
    #Listener for deleted messages
    @commands.Cog.listener()
    async def on_raw_message_delete(self, RawMessageDeleteEvent):
        #Check if the deleted message content was cached
        if RawMessageDeleteEvent.cached_message:
            message = RawMessageDeleteEvent.cached_message
            #Cancel if the message originated from a bot
            #TODO remove when database added
            if message.author.bot:
                return
            message_value = message.content
            #Create the message embed and send it
            embed = self.format_embed(colour=discord.Colour.dark_red(), title="Message deleted", author=message.author, message_id=RawMessageDeleteEvent.message_id)
            embed.add_field(name="Message", value=message.content)
            await message.channel.send(embed=embed)
        #If the deleted message content wasn't cached
        else:
            message_value = "Unknown"
            channel = await self.bot.fetch_channel(RawMessageDeleteEvent.channel_id)
            embed = self.format_embed(colour=discord.Colour.dark_red(), title="Message deleted", author=None, message_id=RawMessageDeleteEvent.message_id)
            embed.add_field(name="Message", value=message_value)
            await channel.send(embed=embed)
        print(f"message was removed in {RawMessageDeleteEvent.channel_id}")

async def setup(bot):
    await bot.add_cog(messageLogging(bot))