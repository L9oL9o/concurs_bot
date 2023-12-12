from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from handlers.users.text import start_command_text
from keyboards.inline.start_inline import generate_channels_keyboard
from loader import dp

@dp.message_handler(CommandStart())
async def handle_start(message: types.Message):
    keyboard = generate_channels_keyboard()
    await message.answer(text=start_command_text, reply_markup=keyboard)
