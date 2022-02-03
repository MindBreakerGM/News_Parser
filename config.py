import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('BOT_TOKEN')

CHAT_ID = os.getenv('CHAT_ID')

NEWS_POST = """
📰Новости Москвы.
\n
👀Политика.
{0}
🎭Общественные резонансы.
{1}
🏙В городе.
{2}
"""