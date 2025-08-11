import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.bot_config import BOT_TOKEN
from handlers import register_all_handlers
from database.models import init_db

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

async def on_startup(_):
    # Initialize database
    await init_db()
    # Register all handlers
    register_all_handlers(dp)
    print('Bot started successfully!')

def main():
    # Start bot
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

if __name__ == '__main__':
    main()