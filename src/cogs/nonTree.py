from discord.ext import commands

class nonTree(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #sync tree, only the bot owner can use this command
    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        await self.bot.tree.sync()
        await ctx.send("Synced tree!")
        print("synced tree")
    #ping command, responds with pong
    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("Pong!")
        print("sent pong")

async def setup(bot):
    await bot.add_cog(nonTree(bot))