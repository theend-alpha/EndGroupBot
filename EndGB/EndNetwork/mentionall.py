from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila

@Crystal.on_message(filters.command(["all", "tagall"]) & filters.group & ~filters.edited & ~filters.forwarded & ~filters.via_bot)
async def all(Kiddo, taenii: Aila):
    if len(taenii.command) >= 2:
        arre = taenii.text.split(None, 1)[1]
        hehe = arre
    else:
        hehe = "Hello everyone"
    mentions = """"""
    LOL = []
    async for user in Kiddo.iter_chat_members(taenii.chat.id):
        mention = user.user.username
        if mention != None:
            if "bot" in mention.lower():
                return
            else:
                LOL.append(mention)
        for tara in LOL:
            mentions += f"\n@{tara}"           
    lel = f"{hehe}\n{mentions}"
    await Kiddo.send_message(taenii.chat.id, lel) 
    
