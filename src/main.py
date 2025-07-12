import os
import sys
import asyncio

from dotenv import load_dotenv
from bojango.core.bot import BojangoBot, BojangoBotConfig


load_dotenv()
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


config = BojangoBotConfig(
    api_token=os.getenv('TELEGRAM_TOKEN'),
    handlers_modules=[
        'handlers.commands',
        'handlers.messages',
        'handlers.callback.screens',
        'handlers.callback.logical',
    ]
)


async def main():
    bot = BojangoBot(config)
    try:
        print('Запуск бота...')
        await bot.start()
        print('Бот запущен.')
    finally:
        await bot.stop()
        print('Бот остановлен.')

if __name__ == '__main__':
    asyncio.run(main())