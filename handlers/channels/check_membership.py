# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.types import ChatMemberStatus
# from aiogram.utils import executor
#
# from data.config import CHANNELS_LINKS
#
# API_TOKEN = 'your_bot_token'
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
#
# async def is_user_member(user_id, channel_id):
#     try:
#         # Use get_chat_member to get information about the user's status in the channel
#         chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
#
#         # Check if the user is a member of the channel
#         return chat_member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR]
#
#     except Exception as e:
#         # Handle exceptions (e.g., user not found or bot not in the channel)
#         print(f"Error checking membership: {e}")
#         return False
#
#
# @dp.message_handler(commands=['check_membership'])
# async def handle_check_membership(message: types.Message):
#     # Specify the user ID and channel ID
#     user_id = message.from_user.id
#     channel_id = CHANNELS_LINKS
#
#     # Check if the user is a member of the channel
#     is_member = await is_user_member(user_id, channel_id)
#
#     # Respond to the user based on the membership status
#     if is_member:
#         await message.answer("You are a member of the channel.")
#     else:
#         await message.answer("You are not a member of the channel.")
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
