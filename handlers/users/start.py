from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from handlers.channels.channels_link import channels_links
from handlers.users.text import start_command_text
from keyboards.inline.start_inline import generate_channels_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def handle_start(message: types.Message):
    keyboard = generate_channels_keyboard()
    await message.answer(text=start_command_text, reply_markup=keyboard)


# @dp.message_handler(text="add_channel")
# async def add_admin_channel(message: types.Message):
#     await message.answer(text="")

database = {}
# database = channels_links



# checking is admin or user (didn't work)
@dp.message_handler(commands="add_channel")
async def admin_add_channel(message: types.Message):
    admin_id = ADMINS
    user_id = str(message.from_user.id)
    if user_id == admin_id:
        await message.answer("Send me the URL of channel")

        # print(1, type(message), type("==761632123 ADMIN"))
        # print(message.text)
        channel_link = message.text
        print(channel_link)
        channel = database.get('channels')
        if channel:
            database['channels'].append(channel_link)
            await message.answer("you are admin, and channel added")
        else:
            database["channels"] = [channel_link]
    elif user_id != admin_id:
        await message.answer(text="You aren't admin \n")
        print(message.from_user.id, "!=761632123 ADMIN \n")
        print(2, type(message), type("==761632123 \n"))
        print(type(user_id), type(admin_id))




# # Обработчик команды
# def handle_command(update, context):
#     user_id = update.message.from_user.id
#
#     # Проверяем, является ли пользователь администратором
#     if user_id in ADMINS:
#         # Пользователь - администратор, обрабатываем команду
#         update.message.reply_text("Вы ввели команду для администратора.")
#         # Ваш код для команды от админа
#     else:
#         # Пользователь - не администратор, не реагируем на команду
#         update.message.reply_text("Вы не являетесь администратором. Команда не выполнена.")
