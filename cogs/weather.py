import logging
import discord
from discord import app_commands, Embed
from discord.ext import commands
import aiohttp
import datetime 
from utils.api_data import get_coordinates, get_weather
from database import model

logger = logging.getLogger(__name__)

class WeatherCog(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot
        self.db = bot.db

    @app_commands.command(name="weather", description="Pobiera dane pogodowe dla podanego miasta")
    @app_commands.describe(city_name="Nazwa miasta do sprawdzenia")
    async def weather(self, interaction: discord.Interaction, city_name: str) :
     
        embed: Embed = discord.Embed(title=f"Pogoda", color=4539717, timestamp=datetime.datetime.now())
        
        try:
            await interaction.response.defer()

            async with aiohttp.ClientSession() as session:
                coords = await get_coordinates(session, city_name)
                
                if not coords:
                    await interaction.followup.send("Nie znaleziono podanego miasta.")
                    return

                lat, lon, full_name = coords

                weather_data = await get_weather(session, lat, lon)
                
                if not weather_data or 'current_weather' not in weather_data:
                    await interaction.followup.send("Nie udało się pobrać danych pogodowych.")
                    return

                current = weather_data['current_weather']
                temp = current['temperature']
                wind = current['windspeed']

                embed.title = f"Pogoda dla: {full_name}"
                embed.description = f"Współrzędne: {lat}, {lon}"
                embed.add_field(name="🌡️ Temperatura", value=f"{temp} °C", inline=True)
                embed.add_field(name="💨 Wiatr", value=f"{wind} km/h", inline=True)
                new_record = {
                    "city": full_name,
                    "temperature": str(temp),
                    "windspeed": str(wind),
                    "timestamp": int(datetime.datetime.now().timestamp())
                }
                
                self.db.create(model.history_class('history'), new_record)

                await interaction.followup.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Error", description=str(e), color=0xFF0000)
            await interaction.followup.send(embed=embed, ephemeral=True)
            logger.critical("%s[%s] raise critical exception - %r", interaction.user.name, interaction.user.id, e)

        finally:
            logger.info("%s issued bot command: /weather", interaction.user.name)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WeatherCog(bot))