from aiogram import Router, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command


menu_router = Router()
CHAT_ID = "-4845386829" 


# Создание reply-клавиатуры
def get_main_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="/photo"), KeyboardButton(text="/flash")],
        [KeyboardButton(text="/video"), KeyboardButton(text="/start")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# Обработчик команды /start
@menu_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Добро пожаловать в ESP32-CAM Telegram бот!\n"
        "Используйте кнопки ниже для управления устройством.",
        reply_markup=get_main_keyboard()
    )

# Обработчик команд /photo, /flash, /video
@menu_router.message(Command(commands=["photo", "flash", "video"]))
async def handle_commands(message: types.Message):
    command = message.text
    await message.bot.send_message(chat_id=CHAT_ID, text=command)
    await message.answer(f"Команда {command} отправлена устройству.", reply_markup=get_main_keyboard())

# Обработчик текстовых сообщений (для кнопок)
@menu_router.message()
async def handle_text(message: types.Message):
    text = message.text
    if text in ["/photo", "/flash", "/video", "/start"]:
        await message.bot.send_message(chat_id=CHAT_ID, text=text)
        await message.answer(f"Команда {text} отправлена устройству.", reply_markup=get_main_keyboard())
    else:
        await message.answer("Пожалуйста, используйте кнопки или команды.", reply_markup=get_main_keyboard())

