from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from YashviK import yashu

STGRP = """

Hey {}!! 💫{}✨ Is Alive .\n\n Used to generate string session.

"""

ALPHA_PIC = "https://te.legra.ph/file/9a207e6e453a93ab2b165.jpg"

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def yashualpha():
    await client.send_file(ALPHA_PIC, caption=Data.START.format(msg.from_user.mention, mention), reply_markup=InlineKeyboardMarkup(Data.buttons))
