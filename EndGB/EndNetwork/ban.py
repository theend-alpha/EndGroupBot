from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev

BAN_TEXT = "{} is banned by {} !"

@End.on_message(filters.command("ban") & filters.group & ~filters.forwarded & ~filters.edited & ~filters.via_bot)
async def ban(alpha, keshav: Dev):
