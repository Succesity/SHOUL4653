import discord
from discord.ext import commands
import logging
import traceback
import sys

import config

log = logging.getLogger(__name__)

initial_extensions = (
    'cogs.base_cog',
    'cogs.more_commands_cog',
)


class AquaBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config.prefix , help_command=None)

        self.client_id = config.client_id

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()

if __name__ == "__main__":
    bot = AquaBot()
    bot.run(config.token)
