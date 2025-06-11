from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command


menu_router = Router()

keyboard_menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Получить фото'), KeyboardButton(text='Получить видео'), KeyboardButton(text='Опрос датчиков')],
        [KeyboardButton(text='Выход')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню',
    one_time_keyboard=False
)

@menu_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот ESP32-CAM!!!\nДля управления воспользуйтесь клавиатурой',
                         reply_markup=keyboard_menu
                         )

@menu_router.message(F.text =='Получить фото')
async def get_foto(message: Message):
    await message.answer('Запрос фото отправлен на ESP32-CAM...', reply_markup=keyboard_menu)
    
@menu_router.message(F.text =='Получить видео')
async def get_video(message: Message):
    await message.answer('Запрос видео отправлен на ESP32-CAM...', reply_markup=keyboard_menu)

@menu_router.message(F.text =='Опрос датчиков')
async def cmd_reading(message: Message):
    await message.answer('Запрос состояния датчика PIR отправлен...', reply_markup=keyboard_menu)

@menu_router.message(F.text =='Exit')
async def cmd_exit(message: Message):
    await message.answer('Вы вышли из бота!👣👣👣\nДля возвращения к боту выполнинте команду "/start".\nДо свидания, всего наилучшего!👋',
                         reply_markup=ReplyKeyboardRemove())
    

