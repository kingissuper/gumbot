from discord import Intents
from discord.ext import commands
from os import environ as env

import cogs
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=env.get("COMMAND_PREFIX"), intents=Intents.all(), owner_id=int(env.get("OWNER_ID")))
        self.token = env.get("TOKEN")

    def run(self):
        super().run(self.token, reconnect=True)
        
    async def on_ready(self):
        print(f'Logged in as {self.user.name} - {self.user.id}')
        #Load cogs dynamically
        #In on_ready because it needs to be in an async function
        for cog in cogs.__all__:
            await self.load_extension(cog.__name__)
            print(f"Loaded cog: {cog.__name__}")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
