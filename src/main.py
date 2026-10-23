from discord import Intents
from discord.ext import commands
from os import environ as env

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=env.get("COMMAND_PREFIX"), intents=Intents.all(), owner_id=int(env.get("OWNER_ID")))
        print(self.command_prefix)
        self.token = env.get("TOKEN")

    def run(self):
        super().run(self.token, reconnect=True)
        
    async def on_ready(self):
        print(f'Logged in as {self.user.name} - {self.user.id}')
        import cogs
        for cog in cogs.__all__:
            await cog.setup(self)
            print(f"Loaded cog: {cog.__name__}")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
