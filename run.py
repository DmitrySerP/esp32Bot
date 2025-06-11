import asyncio
from aiogram import F, Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from menu import menu_router


dp = Dispatcher()


async def main():
    bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode= ParseMode.MARKDOWN))
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_router(menu_router)
    await dp.start_polling(bot)
    
async def startup(dispatcher: Dispatcher):
    print('Starting bot...')

async def shutdown(dispatcher:Dispatcher):
    print('Stopped bot!')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    