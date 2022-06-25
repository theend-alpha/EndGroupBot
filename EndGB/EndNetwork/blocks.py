from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndDB import *

@Crystal.on_message(filters.command("block") & filters.group & ~filters.forwarded & ~filters.edited)
async def block(_, m: Aila):
    if is_sudo(m.from_user.id) is True:
        if len(m.command) == 2:
            id = int(m.text.split(None, 1)[1])
        else:
            id = m.reply_to_message.from_user.id
        mention = (await _.get_users(id)).mention
        if is_blocked(id) is False:
            block_user(id)
            await m.reply(f"{mention} blocked to use crystal")
        else:
            await m.reply("this user already blocked")

@Crystal.on_message(filters.command("unblock") & filters.group & ~filters.forwarded & ~filters.edited)
async def unblock(_, m: Aila):
    if is_sudo(m.from_user.id) is True:
        if len(m.command) == 2:
            id = int(m.text.split(None, 1)[1])
        else:
            id = m.reply_to_message.from_user.id
        mention = (await _.get_users(id)).mention
        if is_blocked(id) is True:
            unblock_user(id)
            await m.reply(f"{mention} unblocked")
        else:
            await m.reply("this user is not blocked")

@Crystal.on_message(filters.command("blocked") & ~filters.forwarded & ~filters.edited)
async def listblock(_, m: Aila):
    if is_sudo(m.from_user.id) is True:
        blocked = list_all_blocked()
        msg = """"""
        for block in blocked:
            name = (await _.get_users(block.i)).first_name
            msg += f"\n• {name} ({block.i}) \n"
        lel = f"**Blocked** :- \n\n{msg}\n\n **Count** :-{len(blocked)}"
        await m.reply(lel)

    
