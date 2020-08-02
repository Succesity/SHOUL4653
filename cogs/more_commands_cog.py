import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import asyncio

import modules.CONSTANTS as CONSTANTS

import config

PREFIX = CONSTANTS.PREFIX


class MoreCommandsCog(commands.Cog, name="MoreCommands"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def nuevostatus(self, ctx):
        args = ctx.message.content.split(" ")[1:]
        text = " ".join(args)
        stream = discord.Streaming(name=text, url="https://www.twitch.tv/fanhots")
        await self.bot.change_presence(activity=stream)


    @commands.command()
    async def avatar(self, ctx):
        args = ctx.message.content.split(" ")[1:]
        embed = discord.Embed()
        embed.colour = discord.Color.from_rgb(0, 255, 255)

        if len(args) == 0:
            embed.title = ctx.author.name
            embed.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif len(ctx.message.mentions) > 0:
            for member in ctx.message.mentions:
                embed.title = member.name
                embed.set_image(url=member.avatar_url)
                await ctx.send(embed=embed)
        elif args[0] in ("server", "guild"):
            embed.title = ctx.guild.name
            embed.set_image(url=ctx.guild.icon_url)
            await ctx.send(embed=embed)
        else:
            embed.title = "avatar"
            embed.description = f"Show your avatar, the users mentioned or the server."
            embed.add_field(name="Usage", value=f"{PREFIX}avatar\n{PREFIX}avatar @user1, @user2, ...\n{PREFIX}avatar server", inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MoreCommandsCog(bot))
    print("More Comnands Cog CARGADO")
