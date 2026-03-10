# 🤖 Async Discord Weather & History Bot
> **Bot Discord integrujący asynchroniczne usługi pogodowe z trwałością danych w SQLite.**

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org)
[![Discord.py](https://img.shields.io/badge/library-discord.py-red.svg)](https://discordpy.readthedocs.io/en/stable/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## O projekcie

Projekt stanowi zaawansowaną implementację bota dla platformy Discord, stworzoną w celu demonstracji umiejętności **programowania asynchronicznego** oraz **integracji systemów rozproszonych**. Bot pozwala użytkownikom na pobieranie danych pogodowych w czasie rzeczywistym, jednocześnie zarządzając lokalną bazą danych historycznych.

### 🎯 Kluczowe Wyzwanie Techniczne

W przeciwieństwie do prostych botów, ten projekt rozwiązuje problem **blokowania wątku głównego**. Dzięki zastosowaniu biblioteki `aiohttp` oraz `asyncio`, bot wykonuje zapytania do zewnętrznych API pogodowych w sposób nieblokujący, co pozwala na płynną obsługę wielu serwerów jednocześnie.

---

## 🚀 Kluczowe Funkcjonalności

### 🌡️ Inteligentne Prognozowanie
Bot łączy dane z dwóch niezależnych źródeł API, aby dostarczyć komplet informacji:
* **Geokodowanie (Nominatim API):** Precyzyjne odnalezienie współrzędnych geograficznych (`latitude`, `longitude`) na podstawie nazwy miasta wpisanej przez użytkownika.
* **Pogoda i Środowisko (Open-Meteo API):** Pobieranie temperatury, prędkości wiatru oraz indeksu jakości powietrza (AQI) dla uzyskanych współrzędnych.

### 📜 System Persystencji i Historii
* **Automatyczne Logowanie:** Każde pomyślne wyszukanie jest zapisywane w bazie **SQLite**.
* **Dynamiczne Sortowanie:** Polecenie `/history` wykorzystuje wyrażenia `lambda` do sortowania danych "w locie", prezentując 10 najświeższych wpisów.
* **Unix Timestamps:** Wykorzystanie znaczników czasu Discorda (`<t:TIMESTAMP:f>`), co pozwala każdemu użytkownikowi widzieć datę zapytania w jego własnej strefie czasowej.

---

## 🛠️ Stack Technologiczny

| Technologia | Rola w projekcie |
| :--- | :--- |
| **Python 3.11+** | Fundament aplikacji i logika asynchroniczna |
| **discord.py** | Obsługa protokołu Discord i Slash Commands |
| **aiohttp** | Asynchroniczny klient HTTP do zapytań API |
| **SQLAlchemy** | Mapowanie obiektowo-relacyjne (ORM) dla SQLite |
| **YAML** | Przechowywanie konfiguracji i bezpiecznych tokenów |
| **colorlog** | Wizualna diagnostyka zdarzeń w konsoli |

---

## ⚙️ Instalacja i Konfiguracja

### 1. Przygotowanie aplikacji na Discordzie
Zanim uruchomisz kod, musisz zarejestrować bota w systemie Discord:
1. Przejdź do [Discord Developer Portal](https://discord.com/developers/applications).
2. Kliknij **New Application** i nadaj jej nazwę.
3. W zakładce **Bot**:
   * Skopiuj swój **Token** (będzie potrzebny w pliku `token.yml`).
   * W sekcji **Privileged Gateway Intents** włącz: `Presence Intent`, `Server Members Intent` oraz `Message Content Intent`.
4. W zakładce **OAuth2** -> **URL Generator**:
   * Zaznacz Scope: `bot` oraz `applications.commands`.
   * Zaznacz Bot Permissions: `Administrator` (dla ułatwienia testów) lub odpowiednie uprawnienia do wysyłania wiadomości i embedów.
   * Skopiuj wygenerowany URL i otwórz go w przeglądarce, aby dodać bota na swój serwer.

### 2. Klonowanie projektu
Klonowanie to proces pobrania kopii kodu z GitHuba na Twój lokalny dysk. 
bash
git clone [https://github.com/Marcin10H/DiscordWeatherBot](https://github.com/Marcin10H/DiscordWeatherBot)
cd Discord-Weather-Bot-Async

### 3. Przygotowanie środowiska
python -m venv .venv
# Aktywacja (Windows): .venv\Scripts\activate | (Linux/macOS): source .venv/bin/activate
pip install -r requirements.txt

### 4. Konfiguracja pliku token
1. W folderze assets/ zmień nazwę token.example na token.yml
2. Wklej swój token skopiowany z panelu dewelopera:
TOKEN: "TWÓJ_UNIKALNY_TOKEN_TUTAJ"

## 🎮 Instrukcja Użytkowania
Po uruchomieniu bota komendą python bot.py, używaj następujących poleceń w Discordzie (wpisując /):
- /weather [city_name] – Pobiera pogodę dla miasta (np. /weather city_name: Londyn)
- /history – Wyświetla 10 ostatnich wyszukiwań z bazy danych
- /help – Interaktywne menu pomocy

## 📂 Struktura Katalogów
├── assets/             # Konfiguracja (token.yml)
├── cogs/               # Moduły bota (Cogi) - logika biznesowa
├── database/           # Zarządzanie persystencją (SQLite)
├── logs/               # Logi aplikacji (Daily Rotation)
├── utils/              # Funkcje API i Logger
└── bot.py              # Punkt wejściowy aplikacji

## 🔒 Bezpieczeństwo
Token Protection: Plik assets/token.yml jest dodany do .gitignore, co zapobiega publikacji Twoich prywatnych kluczy dostępowych.
Error Handling: System automatycznie wykrywa błędy API i informuje o nich użytkownika bez przerywania pracy bota.



## 📝 About the Project

This project is an advanced implementation of a Discord bot, created to demonstrate **asynchronous programming** skills and **distributed systems integration**. The bot allows users to fetch real-time weather data while managing a local historical database.

### 🎯 Key Technical Challenge

Unlike simple bots, this project solves the **main thread blocking** problem. By utilizing the `aiohttp` and `asyncio` libraries, the bot performs requests to external weather APIs in a non-blocking manner, allowing for smooth handling of multiple servers simultaneously.

---

## 🚀 Key Features

### 🌡️ Intelligent Forecasting
The bot combines data from two independent API sources to provide comprehensive information:
* **Geocoding (Nominatim API):** Precisely finds geographic coordinates (`latitude`, `longitude`) based on the city name entered by the user.
* **Weather & Environment (Open-Meteo API):** Fetches temperature, wind speed, and Air Quality Index (AQI) for the obtained coordinates.

### 📜 Persistence & History System
* **Automatic Logging:** Every successful search is saved in the **SQLite** database.
* **Dynamic Sorting:** The `/history` command uses `lambda` expressions to sort data "on the fly", displaying the 10 most recent entries.
* **Unix Timestamps:** Utilizes Discord timestamps (`<t:TIMESTAMP:f>`), allowing every user to see the search date in their own local time zone.

---

## 🛠️ Tech Stack

| Technology | Role in Project |
| :--- | :--- |
| **Python 3.11+** | Core application and asynchronous logic |
| **discord.py** | Handling Discord protocol and Slash Commands |
| **aiohttp** | Asynchronous HTTP client for API requests |
| **SQLAlchemy** | Object-Relational Mapping (ORM) for SQLite |
| **YAML** | Configuration and secure token storage |
| **colorlog** | Visual event diagnostics in the console |

---

## ⚙️ Installation and Configuration

### 1. Discord Application Setup
Before running the code, you must register the bot in the Discord system:
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application** and give it a name.
3. In the **Bot** tab:
   * Copy your **Token** (you will need it for the `token.yml` file).
   * In the **Privileged Gateway Intents** section, enable: `Presence Intent`, `Server Members Intent`, and `Message Content Intent`.
4. In the **OAuth2** -> **URL Generator** tab:
   * Select Scopes: `bot` and `applications.commands`.
   * Select Bot Permissions: `Administrator` (for easy testing) or specific permissions for sending messages and embeds.
   * Copy the generated URL and open it in your browser to add the bot to your server.

### 2. Cloning the Project
Cloning is the process of downloading a copy of the code from GitHub to your local disk.
bash
git clone https://github.com/Marcin10H/Discord-Weather-Bot-Async.git
cd Discord-Weather-Bot-Async

### 3. Environment Setup
python -m venv .venv
# Activation (Windows): .venv\Scripts\activate | (Linux/macOS): source .venv/bin/activate
pip install -r requirements.txt

### 4. Token File Configuration
1. In the assets/ folder, rename token.example to token.yml.
2. Paste your token copied from the developer panel:
TOKEN: "YOUR_UNIQUE_TOKEN_HERE"


## 🎮 Usage Instructions
After starting the bot with the command python bot.py, use the following commands in Discord (by typing /):
- /weather [city_name] – Fetches weather for a city (e.g., /weather city_name: London)
- /history – Displays the 10 most recent searches from the database
- /help – Interactive help menu

## 📂 Directory Structure
├── assets/             # Configuration (token.yml)
├── cogs/               # Bot modules (Cogs) - business logic
├── database/           # Persistence management (SQLite)
├── logs/               # Application logs (Daily Rotation)
├── utils/              # API functions and Logger
└── bot.py              # Application entry point

## 🔒 Security
Token Protection: The assets/token.yml file is added to .gitignore, preventing the publication of your private access keys.
Error Handling: The system automatically detects API errors and informs the user without interrupting the bot's operation.

