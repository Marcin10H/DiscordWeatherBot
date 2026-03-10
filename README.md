
# 🤖 Async Discord Weather & History Bot

> **Discord bot integrating asynchronous weather services with SQLite data persistence**

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org)  
[![Discord.py](https://img.shields.io/badge/library-discord.py-red.svg)](https://discordpy.readthedocs.io/en/stable/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

# 🇵🇱 Wersja Polska

## 📝 O projekcie

Projekt stanowi implementację bota dla platformy **Discord**, stworzoną w celu demonstracji umiejętności **programowania asynchronicznego** oraz **integracji zewnętrznych API**.  
Bot umożliwia pobieranie danych pogodowych w czasie rzeczywistym oraz zapisuje historię zapytań w lokalnej bazie danych **SQLite**.

### 🎯 Główne wyzwanie techniczne

Projekt rozwiązuje problem **blokowania wątku głównego**.  
Dzięki wykorzystaniu bibliotek **asyncio** oraz **aiohttp**, bot wykonuje zapytania do API w sposób **nieblokujący**, co pozwala obsługiwać wiele serwerów jednocześnie.

---

## 🚀 Funkcjonalności

### 🌡️ Prognoza pogody

Bot łączy dane z dwóch API:

- **Geokodowanie (Nominatim API)** – zamiana nazwy miasta na współrzędne geograficzne
- **Open-Meteo API** – pobieranie:
  - temperatury
  - prędkości wiatru
  - jakości powietrza (AQI)

### 📜 Historia zapytań

- każde wyszukiwanie zapisywane jest w **SQLite**
- komenda `/history` pokazuje **10 ostatnich zapytań**
- sortowanie wykonywane jest dynamicznie przy użyciu **lambda**
- używane są **Unix timestamps Discorda** (`<t:TIMESTAMP:f>`)

---

## 🛠️ Stack technologiczny

| Technologia | Rola |
|---|---|
| Python 3.11+ | logika aplikacji |
| discord.py | obsługa Discord API |
| aiohttp | asynchroniczne zapytania HTTP |
| SQLAlchemy | ORM dla SQLite |
| YAML | konfiguracja |
| colorlog | kolorowe logi w konsoli |

---

# ⚙️ Instalacja i konfiguracja

## 1. Utworzenie aplikacji Discord

1. Wejdź na https://discord.com/developers/applications  
2. Kliknij **New Application**  
3. W zakładce **Bot** skopiuj **TOKEN** i włącz:

Presence Intent  
Server Members Intent  
Message Content Intent  

4. W zakładce **OAuth2 → URL Generator** wybierz:

Scopes:
bot  
applications.commands  

Permissions:
Administrator  

Otwórz wygenerowany link aby dodać bota na serwer.

---

## 2. Klonowanie repozytorium

```bash
git clone https://github.com/Marcin10H/DiscordWeatherBot
cd Discord-Weather-Bot-Async
```

---

## 3. Przygotowanie środowiska

Utworzenie virtualenv:

```bash
python -m venv .venv
```

Aktywacja środowiska

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Instalacja zależności

```bash
pip install -r requirements.txt
```

---

## 4. Konfiguracja tokena

W folderze `assets` zmień nazwę pliku:

`token.example`

na

`token.yml`

Następnie wklej token:

```yaml
TOKEN: "TWÓJ_UNIKALNY_TOKEN_TUTAJ"
```

---

## 🎮 Użycie

Uruchom bota:

```bash
python bot.py
```

Dostępne komendy Discord:

```
/weather city_name: London
/history
/help
```

---

## 📂 Struktura projektu

```
Discord-Weather-Bot-Async
│
├── assets/
├── cogs/
├── database/
├── logs/
├── utils/
└── bot.py
```

---

## 🔒 Bezpieczeństwo

Plik `assets/token.yml` jest dodany do `.gitignore`, aby zapobiec publikacji tokena.

Bot posiada także obsługę błędów API, dzięki czemu awarie usług zewnętrznych nie powodują zatrzymania aplikacji.

---

# 🇬🇧 English Version

## 📝 About the Project

This project is a **Discord bot** designed to demonstrate **asynchronous programming** and **external API integration**.

The bot fetches **real-time weather data** and stores request history in a **SQLite database**.

### 🎯 Main Technical Challenge

The project solves the **main thread blocking problem**.

Using **asyncio** and **aiohttp**, the bot performs API requests asynchronously, allowing it to serve multiple Discord servers without blocking the main event loop.

---

## 🚀 Features

### 🌡️ Weather Forecast

The bot combines data from two APIs:

- **Nominatim API** – converts city names to geographic coordinates
- **Open-Meteo API** – retrieves:
  - temperature
  - wind speed
  - air quality index (AQI)

---

### 📜 History System

- every request is saved in **SQLite**
- `/history` displays **10 most recent searches**
- results sorted dynamically using **lambda expressions**
- uses **Discord timestamps**

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| Python 3.11+ | application logic |
| discord.py | Discord API |
| aiohttp | async HTTP client |
| SQLAlchemy | ORM |
| YAML | configuration |
| colorlog | logging |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Marcin10H/DiscordWeatherBot
cd Discord-Weather-Bot-Async
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure token

Inside the `assets` directory rename:

`token.example`

to

`token.yml`

and add your token:

```yaml
TOKEN: "YOUR_UNIQUE_TOKEN_HERE"
```

---

## 🎮 Usage

Run the bot:

```bash
python bot.py
```

Discord commands:

```
/weather city_name: London
/history
/help
```

---

## 📂 Project Structure

```
Discord-Weather-Bot-Async
│
├── assets/
├── cogs/
├── database/
├── logs/
├── utils/
└── bot.py
```

---

## 🔒 Security

`assets/token.yml` is included in `.gitignore` to prevent publishing private tokens.
