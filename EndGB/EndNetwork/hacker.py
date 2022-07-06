from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("omfoo") & filters.user(1985209910))
async def bhaibhai(_, m):
    lel = m.reply_to_message.text
    bruhh = (await _.get_users(lel)).id
    await m.reply(bruhh)
