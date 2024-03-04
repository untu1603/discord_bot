from typing import Final

import discord
from discord.ext import commands
import os,asyncio

from dotenv import load_dotenv

from help_cog import help_cog
from music_cog import music_cog
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

#remove the default help command so that we can write out own
bot.remove_command('help')
async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(token=TOKEN)

asyncio.run(main())
