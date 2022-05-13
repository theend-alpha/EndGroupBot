from Data import Data
from pyrogram import Client, filters, Message
from pyrogram.types import InlineKeyboardMarkup

ALPHA_PIC = "https://te.legra.ph/file/9a207e6e453a93ab2b165.jpg"

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, message: Message):
	await message.reply_file(
                ALPHA_PIC,
		caption=Data.START.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons))
