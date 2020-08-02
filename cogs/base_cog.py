import discord
from discord.ext import commands
import asyncio
import requests

import modules.CONSTANTS as CONSTANTS

PREFIX = CONSTANTS.PREFIX

class BaseCog(commands.Cog, name="Base"):
    def __init__(self, bot):
        self.bot = bot
        self.updating = self.bot.loop.create_task(self.infinite_messages())
        #self.updating = self.bot.loop.create_task(self.update_stats())

    @commands.Cog.listener()
    async def on_ready(self):
        print("El bot se ha iniciado correctamente.")
        print(self.bot.user)

        #game = discord.Game(f"{PREFIX}help | {len(self.bot.guilds)} servers")
        #await self.bot.change_presence(status=discord.Status.online, activity=game)

        stream = discord.Streaming(name="._.XD",url="https://www.twitch.tv/rubius")

        await self.bot.change_presence(activity=stream)

    async def infinite_messages(self):
        await asyncio.sleep(10)
        user = self.bot.get_user(405339224125210625)
        print(user)

        while not self.bot.is_closed():
            await asyncio.sleep(2)
            await user.send("ekisde")

    # async def update_stats(self):
    #     while not self.bot.is_closed():
    #         await asyncio.sleep(1800)

    #         headers = {
    #             "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGkiOnRydWUsImlkIjoiNDAyMjkxMzUyMjgyNDY0MjU5IiwiaWF0IjoxNTczNDA1OTQ1fQ.5F02lOOyINjsxWoSjRmkJPY7MMp15U2zgBX52TgkQwk"
    #         }
    #         data = {
    #             "guildCount": len(self.bot.guilds)
    #         }
    #         r = requests.post("https://discord.bots.gg/api/v1/bots/518213843344687130/stats", json=data, headers=headers)
    #         print("DISCORD.BOTS.GG: " + str(r.status_code))

    #         headers = {
    #             "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUxODIxMzg0MzM0NDY4NzEzMCIsImJvdCI6dHJ1ZSwiaWF0IjoxNTczNDA3NDY2fQ.5qdtlUTjgI1awGg0tHqeVXAhOj5DVFljXhuRVtMWDL0"
    #         }
    #         data = {
    #             "server_count": len(self.bot.guilds)
    #         }
    #         r = requests.post("https://top.gg/api/bots/518213843344687130/stats", json=data, headers=headers)
    #         print("TOP.GG: " + str(r.status_code))


def setup(bot):
    bot.add_cog(BaseCog(bot))
    print("Base Cog CARGADO")

