from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

STGRP = """

Hey {}!! 💫{}✨ Is Alive .\n\n Used to generate string session.

"""

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		msg.chat.id,
		Data.START.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)

@Client.on_message(filters.group & filters.edited & ~filters.private & filters.command(get_command("start")))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
                STGRP.format(msg.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup ([
     
                     [
                     InlineKeyboardButton("✨Owner❤️", url=f"t.me/NotReallyAlpha")
                     ],
                     [
                     InlineKeyboardButton("✨Updater🤍", url=f"t.me/NotReallyMani"),
                     InlineKeyboardButton("✨Group💜", url=f"t.me/BTS_CHAT_ZONE")
                     ],
                     [
                     InlineKeyboardButton("✨Click here to start💫", url=f"t.me/EndStringBot")
                     ]
         ])

	)
