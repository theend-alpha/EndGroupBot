from Yashvi import Keshav
from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

photo = "https://te.legra.ph/file/1fec31d4b0f3700dc9e90.jpg"

@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, message: Message):
   user = await bot.get_me()
   mention = user["mention"]
   await message.reply_photo(
      photo,
      caption=Keshav.ALPHAVERSION)
