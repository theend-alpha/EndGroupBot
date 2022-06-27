from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndDB.servers_cdb import *

@Crsytal.on_message(group=1)
async def cwfunc(_, m):
    chat_id = m.chat.id
    if is_served_chat(chat_id):
        return
    add_served_chat(chat_id)
