from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndDB.blocks_cdb import *
from EndGB.EndDB.sudos_cdb import *
from EndGB.EndNetwork.sudos import ALPHA_ID

@Crystal.on_message(filters.command("block") & filters.group & ~filters.forwarded & ~filters.edited)
async def block(_, m: Aila):
    if is_sudo(m.from_user.id) is True or m.from_user.id in ALPHA_ID:
        if len(m.command) == 2:
            id = int(m.text.split(None, 1)[1])
        else:
            id = m.reply_to_message.from_user.id
        if is_sudo(id) is True:
            return await m.reply("this user is a sudo, you can't block them")
        elif id in ALPHA_ID:
            return await m.reply("Bruhh! He's the owner of this bot 🤧")
        u_n = (await _.get_users(id)).username
        if "bot" in u_n:
            return
        else:
            mention = (await _.get_users(id)).mention
        if is_blocked(id) is False:
            block_user(id)
            await m.reply(f"{mention} blocked to use crystal")
        else:
            await m.reply("this user is already blocked")

@Crystal.on_message(filters.command("unblock") & filters.group & ~filters.forwarded & ~filters.edited)
async def unblock(_, m: Aila):
    if is_sudo(m.from_user.id) is True or m.from_user.id in ALPHA_ID:
        if len(m.command) == 2:
            id = int(m.text.split(None, 1)[1])
        else:
            id = m.reply_to_message.from_user.id
        if id in ALPHA_ID:
            return await m.reply("lol 🤧😂")
        mention = (await _.get_users(id)).mention
        if is_blocked(id) is True:
            unblock_user(id)
            await m.reply(f"{mention} unblocked")
        else:
            await m.reply("this user is not in blocklist")

@Crystal.on_message(filters.command("blocked") & ~filters.forwarded & ~filters.edited)
async def listblock(_, m: Aila):
    if is_sudo(m.from_user.id) is True or m.from_user.id in ALPHA_ID:
        blocked = list_all_blocked()
        msg = """"""
        for block in blocked:
            name = (await _.get_users(block.id)).first_name
            msg += f"\n• {name} ({block.id}) \n"
        if len(blocked) == 0:
            await m.reply("no blocked users")
        else:
            lel = f"**Blocked** :- \n\n{msg}\n\n **Count** :- {len(blocked)}"
            await m.reply(lel)

    
