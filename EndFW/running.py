import datetime
from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev
import random

LIST = [["https://te.legra.ph/file/824249a676c2f7d905d0a.jpg", "january"], ["https://te.legra.ph/file/0e41873bc5474eedcb892.jpg", "may"]]

@End.on_message(filters.command("ready"))
async def ready(_, m: Dev):
    global temxt
    now = datetime.datetime.now()
    while now.minute == 15:
        LIMST = random.choice(LIST)
        pomto = LIMST[0]
        temxt = LIMST[1] 
        await _.send_photo(m.chat.id, pomto, caption="Write this word")
 
@End.on_message(filters.text & ~filters.edited & ~filters.forwarded & ~filters.via_bot & filters.group)
async def chat_watcher(_, m: Dev):
    hehe = m.text
    omfoo = m.command
    if m.command != 1:
        return
    elif m.command == 1 and m.text == temxt:
        await m.reply("bot working")
