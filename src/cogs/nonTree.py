from discord.ext import commands
class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def sync(self, ctx):
        await self.tree.sync()
        await ctx.send("Synced tree!")
    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("Pong!")

async def setup(bot):
    await bot.add_cog(Cog(bot))