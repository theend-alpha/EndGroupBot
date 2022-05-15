from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

photo = "https://te.legra.ph/file/efecf136bc78da25719fd.jpg"

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, message: Message):
   user = await bot.get_me()
   mention = user["mention"]
   await message.reply_photo(
      photo,
      caption=Data.START.format(message.from_user.mention, mention),
      reply_markup=InlineKeyboardMarkup(Data.buttons))
