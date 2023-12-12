from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.channels.channels_link import channels_links

db = channels_links


# Function to generate InlineKeyboardMarkup with buttons for channels
def generate_channels_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)

    # Iterate over the list of channels
    for channel_url in channels_links:
        keyboard.add(InlineKeyboardButton(text="🥷 Obuna Bo'ling !!!", url=channel_url))

    # Add a button for confirming subscription to all channels
    keyboard.add(InlineKeyboardButton(text="✅  Tasdiqlsh", callback_data="subscribe_all"))

    return keyboard


""" 🥷  ✅ """