import logging
import discord
from discord import app_commands, Embed
from discord.ext import commands
import datetime
from database import model 

logger = logging.getLogger(__name__)

class HistoryCog(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot
        self.db = bot.db

    @app_commands.command(name="history", description="Historia 10 ostatnich wyszukiwań pogody")
    async def history(self, interaction: discord.Interaction) :
        embed: Embed = discord.Embed(title="Ostatnie wyszukiwania", description="Lista 10 ostatnich zapytań o pogodę",
                                     color=4539717, timestamp=datetime.datetime.now())
        try:
            await interaction.response.defer()

            history_data = self.db.select(model.history_class('history'))

            if not history_data:
                embed.description = "Brak historii wyszukiwań."
                await interaction.followup.send(embed=embed)
                return

            sorted_history = sorted(history_data, key=lambda x: x['timestamp'], reverse=True)

            last_10 = sorted_history[:10]

            for entry in last_10:
                city = entry['city']
                temp = entry['temperature']
                ts = entry['timestamp']
                
                discord_time = f"<t:{ts}:f>"
                
                embed.add_field(
                    name=city, 
                    value=f"Temp: {temp}°C | Data: {discord_time}", 
                    inline=False
                )

            await interaction.followup.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=str(e), color=0xFF0000)
            await interaction.followup.send(embed=embed, ephemeral=True)
            logger.critical("%s[%s] raise critical exception - %r", interaction.user.name, interaction.user.id, e)

        finally:
            logger.info("%s issued bot command: /history", interaction.user.name)

async def setup(bot: commands.Bot) :
    await bot.add_cog(HistoryCog(bot))