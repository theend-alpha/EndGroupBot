from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev

@End.on_message(filters.command(["start", f"start@{bn}"]) & ~filters.edited & ~filters.forwarded & ~filters.via_bot)
async def (Alpha, Doli: Dev):
    uid = Doli.from_user.id
    nayan = await Alpha.get_users(uid)
    tara = nayan.mention
