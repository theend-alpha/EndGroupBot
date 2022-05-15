from Yashvi import Keshav
from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup

photo = "https://te.legra.ph/file/1fec31d4b0f3700dc9e90.jpg"

@Client.on_message(filters.private & filters.incoming & filters.command("alphaversion"))
async def _alphaversion(bot, msg):
    await msg.reply_photo(photo,
        Keshav.ALPHAVERSION,
        disable_web_page_preview=True,
    )
