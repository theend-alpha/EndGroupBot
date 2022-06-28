from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndDB.sudos_cdb import *

ALPHA_ID = [1985209910]

@Crystal.on_message(filters.command("addc") & filters.group & filters.user(ALPHA_ID) & ~filters.forwarded & ~filters.edited)
async def addc(deadbody, Alpha: Aila):
    if len(Alpha.command) == 2:
        id = int(Alpha.text.split(None, 1)[1])
    else:
        id = Alpha.reply_to_message.from_user.id
    if Alpha.reply_to_message:
        u_n = Alpha.reply_to_message.from_user.username
    elif len(Alpha.command) == 2:
        u_n = (await deadbody.get_users(id)).username
    if u_n:
        if "bot" in u_n.lower():
            return
        lel = "@" + u_n
    else:
        lel = Alpha.reply_to_message.from_user.mention
    if is_sudo(id) is False:
        add_sudo(id)
        await Alpha.reply(f"{lel} is added as sudo")
    else:
        await Alpha.reply("This user is already a sudo")

@Crystal.on_message(filters.command("delc") & filters.group & filters.user(ALPHA_ID) & ~filters.forwarded & ~filters.edited)
async def delc(deadbody, Alpha: Aila):
    if len(Alpha.command) == 2:
        id = int(Alpha.text.split(None, 1)[1])
    else:
        id = Alpha.reply_to_message.from_user.id
    if Alpha.reply_to_message:
        u_n = Alpha.reply_to_message.from_user.username
    elif len(Alpha.command) == 2:
        u_n = (await deadbody.get_users(id)).username
    if u_n:
        lel = "@" + u_n
    else:
        lel = Alpha.reply_to_message.from_user.mention
    if is_sudo(id) is True:
        del_sudo(id)
        await Alpha.reply(f"{lel} is removed as sudo")
    else:
        await Alpha.reply("This user is not a sudo")

@Crystal.on_message(filters.command("crystalsudos") & ~filters.edited & ~filters.forwarded)
async def sudos(_, m: Aila):
    if is_sudo(m.from_user.id) is True or m.from_user.id in ALPHA_ID:
        sudos = list_all_sudos()
        msg = """"""
        for sudo in sudos:
            try:
                mention = (await _.get_users(sudo.id)).mention
            except:
                return await m.reply(f"**sudos** :- {len(sudos)}")       
            msg += f"\n• {mention} ({sudo.id})\n"
        if len(sudos) == 0:
            await m.reply("no sudo users")
        else:
            try:
                lol = f"**Crystal Sudos** :- \n\n {msg} \n\n **Count** :- {len(sudos)}"
                await m.reply(lol)
            except:
                await m.reply(f"**sudos** :- {len(sudos)}")

@Crystal.on_message(filters.command("clearall") & filters.user(ALPHA_ID) & ~filters.edited & ~filters.forwarded)
async def clear(_, m: Aila):
    clr_all_sudos()
    await m.reply("All sudos cleared for crystal")
        
