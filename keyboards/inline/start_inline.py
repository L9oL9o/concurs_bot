from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import CHANNELS_LINKS
from handlers.channels.channels_link import channels_links
# from handlers.channels.check_membership import handle_check_membership
from handlers.users.text import follow_command_text, submit_command_text

db = channels_links


# Function to generate InlineKeyboardMarkup with buttons for channels
def generate_channels_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)

    # Iterate over the list of channels
    for channel_url in channels_links:
        keyboard.add(InlineKeyboardButton(text=follow_command_text, url=channel_url))

    # Add a button for confirming subscription to all channels
    keyboard.add(InlineKeyboardButton(text=submit_command_text, callback_data="check_membership"))

    return keyboard


""" 🥷  ✅ """