# from aiogram import types
# from data.config import ADMINS
# from handlers.channels.channels_link import channels_links
# from aiogram.dispatcher import FSMContext
# from aiogram.types import CallbackQuery
#
# from loader import dp, bot
#
# admin_user_id = ADMINS
#
#
#
# def add_channel(channel_name, channel_url):
#     channels_links.append((channel_name, channel_url))
#
# def remove_channel(channel_name):
#     global channels_links
#     channels_links = [(name, url) for name, url in channels_links if name != channel_name]
#
#
# def generate_channels_keyboard(is_admin):
#     keyboard = types.InlineKeyboardMarkup(row_width=1)
#
#     for channel_name, channel_url in channels_links:
#         keyboard.add(types.InlineKeyboardButton(text=channel_name, url=channel_url))
#
#     if is_admin:
#         keyboard.add(types.InlineKeyboardButton(text="Добавить канал", callback_data="add_channel"))
#         keyboard.add(types.InlineKeyboardButton(text="Удалить канал", callback_data="remove_channel"))
#
#     return keyboard
#
#
#
# @dp.callback_query_handler(lambda callback_query: callback_query.data in ["add_channel", "remove_channel"])
# async def process_channel_action(callback_query: CallbackQuery):
#     user_id = callback_query.from_user.id
#     if user_id == admin_user_id:
#         if callback_query.data == "add_channel":
#             # Добавление логики для добавления канала
#             await bot.send_message(user_id, "Введите название и URL канала через пробел.")
#             await YourStateEnum.waiting_for_channel_data.set()
#         elif callback_query.data == "remove_channel":
#             # Добавление логики для удаления канала
#             await bot.send_message(user_id, "Введите название канала для удаления.")
#             await YourStateEnum.waiting_for_channel_name.set()
#     else:
#         await bot.send_message(user_id, "У вас нет прав для выполнения этой операции.")
#
#
#
# @dp.message_handler(state=YourStateEnum.waiting_for_channel_data)
# async def process_channel_data(message: types.Message, state: FSMContext):
#     user_id = message.from_user.id
#     if user_id == admin_user_id:
#         try:
#             channel_name, channel_url = message.text.split()
#             add_channel(channel_name, channel_url)
#             await bot.send_message(user_id, f"Канал '{channel_name}' добавлен.")
#         except ValueError:
#             await bot.send_message(user_id, "Некорректный ввод. Введите название и URL канала через пробел.")
#     else:
#         await bot.send_message(user_id, "У вас нет прав для выполнения этой операции.")
#     await state.finish()
#
# @dp.message_handler(state=YourStateEnum.waiting_for_channel_name)
# async def process_channel_name(message: types.Message, state: FSMContext):
#     user_id = message.from_user.id
#     if user_id == admin_user_id:
#         channel_name = message.text
#         remove_channel(channel_name)
#         await bot.send_message(user_id, f"Канал '{channel_name}' удален.")
#     else:
#         await bot.send_message(user_id, "У вас нет прав для выполнения этой операции.")
#     await state.finish()



from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext

from data.config import ADMINS, BOT_TOKEN
from handlers.channels.channels_link import channels_links

API_TOKEN = BOT_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

admin_user_id = ADMINS  # Замените на фактический user_id админа
channels_link = channels_links

def add_channel(channel_name, channel_url):
    channels_links.append((channel_name, channel_url))

def remove_channel(channel_name):
    global channels_links
    channels_links = [(name, url) for name, url in channels_links if name != channel_name]

def generate_channels_keyboard(is_admin):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    for channel_name, channel_url in channels_links:
        keyboard.add(types.InlineKeyboardButton(text=channel_name, url=channel_url))

    if is_admin:
        keyboard.add(types.InlineKeyboardButton(text="Добавить канал", callback_data="add_channel"))
        keyboard.add(types.InlineKeyboardButton(text="Удалить канал", callback_data="remove_channel"))

    return keyboard

@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    user_id = message.from_user.id
    keyboard = generate_channels_keyboard(user_id == admin_user_id)
    await message.answer("Выберите канал для подписки или подтвердите подписку на все каналы:", reply_markup=keyboard)

@dp.callback_query_handler(lambda callback_query: callback_query.data in ["add_channel", "remove_channel"])
async def process_channel_action(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id == admin_user_id:
        if callback_query.data == "add_channel":
            await bot.send_message(user_id, "Введите название и URL канала через пробел.")
        elif callback_query.data == "remove_channel":
            await bot.send_message(user_id, "Введите название канала для удаления.")
    else:
        await bot.send_message(user_id, "У вас нет прав для выполнения этой операции.")

@dp.message_handler(func=lambda message: message.text.startswith('/add_channel') and message.from_user.id == admin_user_id)
async def add_channel_command(message: types.Message):
    try:
        _, channel_name, channel_url = message.text.split()
        add_channel(channel_name, channel_url)
        await bot.send_message(message.chat.id, f"Канал '{channel_name}' добавлен.")
    except ValueError:
        await bot.send_message(message.chat.id, "Некорректный ввод. Введите '/add_channel Название URL'.")

@dp.message_handler(func=lambda message: message.text.startswith('/remove_channel') and message.from_user.id == admin_user_id)
async def remove_channel_command(message: types.Message):
    try:
        _, channel_name = message.text.split()
        remove_channel(channel_name)
        await bot.send_message(message.chat.id, f"Канал '{channel_name}' удален.")
    except ValueError:
        await bot.send_message(message.chat.id, "Некорректный ввод. Введите '/remove_channel Название'.")

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)