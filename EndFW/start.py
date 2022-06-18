from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev
from Yashvi import Keshav
from Config import BOT_USERNAME as bn

@End.on_message(filters.command(["start", f"start@{bn}"]) & ~filters.edited & ~filters.forwarded & ~filters.via_bot & filters.private)
async def p_start(Alpha, Doli: Dev):
    id = Doli.from_user.id
    nayan = await Alpha.get_users(id)
    tara = nayan.mention
    me = await Alpha.get_me()
    mention = me["mention"]
    add_user(id)
    private_user(id)
    await Doli.reply(Keshav.START_TXT.format(tara, mention), reply_markup=InlineKeyboardMarkup(Keshav.start_markup))

@End.on_message(filters.command(["start", f"start@{bn}"]) & filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded)
async def g_start(Alpha, Doli: Dev):
    id = Doli.from_user.id
    tara = (await Alpha.get_users(id)).mention
    add_user(id)
    await Alpha.send_message(Doli.chat.id, f"Hey! {tara}, start me in pm for help", reply_markup=InlineKeyboardMarkup(" Start ➡️ ", url=f"t.me/{bn}"))
