import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot settings
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
ADMIN_IDS = [int(id) for id in os.getenv('ADMIN_IDS', '').split(',') if id]

# Database settings
DB_URL = os.getenv('DB_URL', 'sqlite://db.sqlite3')

# Checker settings
MAX_THREADS = int(os.getenv('MAX_THREADS', 10))
CHECK_TIMEOUT = int(os.getenv('CHECK_TIMEOUT', 30))
