from pyrogram import Client, filters
from pyrogram.types import Message
ALPHA = [1985209910]

@Client.on_message(filters.command("info") & filters.user(ALPHA))
async def info(_, m):
    if len(m.command) == 2:
        lel = int(m.text.split(None, 1)[1])
        if str(lel)[0] == "-":
            id = lel
        else:
            omfoo = "-" + str(lel)
            id = int(omfoo)

    getter = await _.get_chat(id)
    try:
        link = getter.invite_link
    except:
        link = "None"
    try:
        name = getter.title
    except:
        name = "None"
    await m.reply(f"Group name :- {name}\n\nInvite link :- {link}")
