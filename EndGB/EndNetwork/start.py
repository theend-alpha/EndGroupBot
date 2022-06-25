from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev, InlineKeyboardMarkup, InlineKeyboardButton
from EndGB.EndHelpers import *

DEV_P = "https://te.legra.ph/file/2a431e33cc12f456ec4ce.jpg"

@End.on_message(filters.command(["start", "start@EndCrystalBot"]) & filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded)
async def start(maharaj, Dev):
    await maharaj.send_photo(Dev.chat.id, DEV_P, caption=START_TXT, reply_markup=InlineKeyboardMarkup(START_MARKUP))

@End.on_message(filters.command(["start", "start@EndCrystalBot"]) & filters.group & ~filters.via_bot & ~filters.forwarded)
async def gstart(maharaj, lel: Dev):
    await lel.reply("Ping me for help", reply_markup=InlineKeyboardMarkup(HELP_MARKUP))

@End.on_message(filters.command(["help", "help@EndCrystalBot"]) & filters.private & ~filters.edited)
async def help(_, m: Dev):
    await m.reply(HELP_TXT)
