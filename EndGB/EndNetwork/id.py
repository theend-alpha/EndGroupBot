from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndDB.blocks_cdb import is_blocked

@Crystal.on_message(filters.command(["id", "id@EndCrystalBot"]) & ~filters.edited & ~filters.via_bot)
async def id(_, m: Aila):
    if m.reply_to_message:
        f_n = m.reply_to_message.from_user.first_name
        id = m.reply_to_message.from_user.id
        await m.reply(f"{f_n} has an ID of <code>{id}</code>.")
    else:
        await m.reply(f"user {m.from_user.first_name} has an ID of <code>{m.from_user.id}</code>, chat has an ID <code>{m.chat.id}</code>.")
