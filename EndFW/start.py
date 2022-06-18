from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev
from Yashvi import Keshav

@End.on_message(filters.command(["start", f"start@{bn}"]) & ~filters.edited & ~filters.forwarded & ~filters.via_bot & filters.private)
async def (Alpha, Doli: Dev):
    uid = Doli.from_user.id
    nayan = await Alpha.get_users(uid)
    tara = nayan.mention
    me = await Alpha.get_me()
    mention = me["mention"]
    await Doli.reply(Keshav.START_TXT.format(tara, mention), reply_markup=InlineKeyboardMarkup(Keshav.start_markup))
