from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

START_LINKS = ["https://te.legra.ph/file/ea5ae1ac096f1d9034100.jpg"
               "https://te.legra.ph/file/efecf136bc78da25719fd.jpg"
              ]

photo = random.choice(START_LINKS)

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, message: Message):
   user = await bot.get_me()
   mention = user["mention"]
   await message.reply_photo(
      photo,
      caption=Data.START.format(message.from_user.mention, mention),
      reply_markup=InlineKeyboardMarkup(Data.buttons))
