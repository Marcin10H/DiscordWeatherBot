import logging

import discord
from discord import app_commands, Embed
from discord.ext import commands

import datetime


logger = logging.getLogger(__name__)

class HelpCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="help", description="View information about user account")
    async def help(self, interaction: discord.Interaction) -> None:
        embed: Embed = discord.Embed(title=f"{self.bot.user.name}", description="",
                                     color=4539717, timestamp=datetime.datetime.now())
        try:
            await interaction.response.defer(ephemeral=True)

            embed.title = f"Informacje o koncie {interaction.user.name}:"
            embed.add_field(name="ID:", value=f"{interaction.user.id}", inline=False)
            embed.add_field(name="Język klienta:", value=f"{interaction.locale}", inline=False)

            await interaction.followup.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=str(e), color=0xFF0000)
            await interaction.followup.send(embed=embed, ephemeral=True)
            logger.critical("%s[%s] raise critical exception - %r", interaction.user.name, interaction.user.id, e)

        finally:
            logger.info("%s issued bot command: /help", interaction.user.name)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HelpCog(bot))
