from pyrogram.types import InlineKeyboardButton


class Keshav:
   
    START_TXT = """ Hii !! There {}, I am {} ! \n\n {} will sends a random photo periodically containing some text ! \n\n the user who will writes the word first, will obtain coins\n\n Add me to your group and have fun ! """

    start_markup = [
        [
        InlineKeyboardButton(" ➕ Add in your group ➕ ", url = f"https://t.me/{bn}?startgroup=true")
        ],
        [
        InlineKeyboardButton(" 📖 Help ", callback_data = "help"),
        InlineKeyboardButton(" 🛠 Tutorial ", callback_data = "tutorial")
        ],
        [
        InlineKeyboardButton(" 📝 Info ", callback_data = "info"),
        InlineKeyboardButton(" ✨ Network ", url="t.me/THE_END_NETWORK")
        ]
        ]

        
