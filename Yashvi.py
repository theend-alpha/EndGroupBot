from pyrogram.types import InlineKeyboardButton
from Config import BOT_USERNAME as bn

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

        
    HELP_TXT = """ * Commands help *\n\n • /coins - shows your coins 🪙.\n • /superleague - Shows the top players"""

    TUTORIAL_TXT = """ * Tutorial * \n\n ••> First add me to your group by using add button and then check Help section for commands"""

    INFO_TXT = """ * Developers * \n\n currently developed and maintained by - @Deveshi \n\n belongs to @THE_END_NETWORK \n\n * Credits * \n\n Team ~ @THE_END_NETWORK """

    back_markup = [
        [
        InlineKeyboardButton(" ➕ Add in your group ➕ ", url = f"https://t.me/{bn}?startgroup=true")
        ],
        [
        InlineKeyboardButton(" 🔙 Back ", callback_data = "back")
        ]
        ]
