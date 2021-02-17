import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

admins = [
    1079453114,
    # 61888314
]

contributor = [
    1079453114,
    61888314
]

channels = [
 '@Grammar_Vocabulary_Eng'
]

ip = os.getenv("ip")

db_host = ip  # Если вы запускаете базу не через докер!
# db_host = "db"  # Если вы запускаете базу через докер и у вас в services стоит название базы db

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

I18N_DOMAIN = 'languages'
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{db_host}/{DATABASE}"

