from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndDB.servers_cdb import *

@Crystal.on_message(group=1)
async def cwfunc(_, m):
    chat_id = m.chat.id
    if is_served_chat(chat_id):
        return
    add_served_chat(chat_id)

@Crystal.on_message(filters.command("crystalchats") & ~filters.forwarded)
async def cc(_, m: Aila):
    SCHATS = []
    served = list_schats()
    for serve in served:
        SCHATS.append(serve.id)
    msg = ""
    for SCHAT in SCHATS:
        schat = str(SCHAT)
        msg += f"\n{schat}"
    await m.reply(f"**Served chats** :-\n{msg}\n\n**Count** :- {len(SCHATS)}")

