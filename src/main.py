from discord import Intents
from discord.ext import commands
from os import environ as env
import importlib

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=env.get("COMMAND_PREFIX"), intents=Intents.all(), owner_id=int(env.get("OWNER_ID")))
        self.token = env.get("TOKEN")

    def run(self):
        super().run(self.token, reconnect=True)
        
    async def on_ready(self):
        print(f'Logged in as {self.user.name} - {self.user.id}')
        #Load cogs dynamically
        import cogs
        for cog in cogs.__all__:
            await cog.setup(self)
            print(f"Loaded cog: {cog.__name__}")
        @commands.is_owner()
        async def reload_command(ctx):
            await self.reload_cogs(ctx)
        self.add_command(commands.Command(reload_command, name="reload"))
        
    #AI generated, temporary development command to reload cogs without restarting the bot
    async def reload_cogs(self, ctx):
        import cogs

        for module in cogs.__all__:
            for name, loaded_cog in tuple(self.cogs.items()):
                if loaded_cog.__module__ == module.__name__:
                    await self.remove_cog(name)

            importlib.reload(module)
            await module.setup(self)

        await ctx.send("All cogs reloaded.")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
