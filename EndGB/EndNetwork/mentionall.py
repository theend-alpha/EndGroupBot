from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila

@Crystal.on_message(filters.command(["all", "tagall"]) & filters.group & ~filters.edited & ~filters.forwarded & ~filters.via_bot)
async def all(Kiddo, taenii: Aila):
    if len(taenii.command) >= 2:
        arre = taenii.text.split(None, 1)[1]
        hehe = arre
    else:
        hehe = "Hello everyone"
    users = Kiddo.iter_chat_members(taenii.chat.id)
    mentions = """"""
    for user in users:
        mention = user.user.mention
        mentions += f"\n{mention}"
    lel = f"{hehe}\n{mentions}"
    await Kiddo.send_message(taenii.chat.id, lel) 
    
