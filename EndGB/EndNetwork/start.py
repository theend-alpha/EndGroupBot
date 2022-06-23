from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev, InlineKeyboardMarkup, InlineKeyboardButton
from EndGB.EndHelpers import *

DEV_P = "https://te.legra.ph/file/229d154445b209c57c34d.jpg"

@End.on_message(filters.command(["start", "start@EndCrystalBot"]) & filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded)
async def start(maharaj, Dev):
    await maharaj.send_photo(Dev.chat.id, DEV_P, caption=START_TXT, reply_markup=InlineKeyboardMarkup(START_MARKUP))

@End.on_message(filters.command(["start", "start@EndGroupBot"]) & filters.group & ~filters.via_bot & ~filters.forwarded)
async def gstart(maharaj, Dev):
    await Dev.reply("Ping me for help", reply_markup=InlineKeyboardMarkup(InlineKeyboardButton("Start in Pm", url="t.me/EndGroupBot")))
