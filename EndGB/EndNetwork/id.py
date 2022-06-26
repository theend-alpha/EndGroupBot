from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndDB.blocks_cdb import is_blocked

@Crystal.on_message(filters.command(["id", "id@EndCrystalBot"]) & ~filters.edited & ~filters.via_bot)
async def id(_, m: Aila):
    if m.reply_to_message:
        f_n = m.reply_to_message.from_user.first_name
        id = m.reply_to_message.from_user.id
    else:
        await m.reply("reply to a user")
    await m.reply(f"{f_n} has an id of <code>{id}</code>")
