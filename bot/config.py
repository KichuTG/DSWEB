from os import getenv
from dotenv import load_dotenv
from pathlib import Path

if Path("config.env").exists():
    load_dotenv("config.env")

class Telegram:
    API_ID = int(getenv("API_ID", "28714959"))
    API_HASH = getenv("API_HASH", "c0b9797634090ee3f4c1c56db6c051a7")
    BOT_TOKEN = getenv("BOT_TOKEN", "5289869101:AAHNeUR-S6yun12CzJnUWcqVHbMiLpc2QL8")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "")
    BASE_URL = getenv("BASE_URL", "dramaship.koyeb.app").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://SurfTG:SurfTG@surftg.utrcg.mongodb.net/?retryWrites=true&w=majority&appName=SurfTG")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "-1001547910421").split(",") if channel.strip()]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "Dramaship")
    PASSWORD = getenv("PASSWORD", "Dramaship")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "Dramaship")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "2411061")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = getenv('MULTI_CLIENT', 'False')
    HIDE_CHANNEL = getenv('HIDE_CHANNEL', 'False')
