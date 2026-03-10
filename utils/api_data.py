import aiohttp
import urllib.parse

async def get_coordinates(session: aiohttp.ClientSession, city_name: str):
    city_encoded = urllib.parse.quote(city_name)
    url = f"https://nominatim.openstreetmap.org/search?q={city_encoded}&format=json&limit=1"
    
    headers = {
        "User-Agent": "WeatherBot_Studia/1.0"
    }
    
    try:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                if data:
                    return data[0]['lat'], data[0]['lon'], data[0]['display_name']
            else:
                print(f"Odmowa z Nominatim! Status serwera: {response.status}")
    except Exception as e:
        print(f"Błąd API Nominatim: {e}")
    return None

async def get_weather(session: aiohttp.ClientSession, latitude: str, longitude: str):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
    except Exception as e:
        print(f"Błąd API Open-Meteo: {e}")
    return None