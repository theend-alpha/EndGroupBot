from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev 
from EndGB.EndAddons.emotes import *

@End.on_message(filters.command("doli") & ~filters.edited & ~filters.via_bot)
async def doli(ailika, jhulika: Dev):
        txt = jhulika.text
        if jhulika.command == 1:
            return await jhulika.reply("Try: < /doli crystal >")
        txt = txt.split(None, 1)[1]
        final = ""
        for a in txt:
            a = a.lower()
            a = str(a)
            if a in END_TEXT:
                letter = END_EMOJI[END_TEXT.index(a)]
                final += letter
            else:
                final += a
        await jhulika.reply(final)
