from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndDB.sudos_cdb import *

@Crystal.on_message(filters.command("addc") & filters.group & filters.user(ALPHA_ID) & ~filters.forwarded & ~filters.edited)
async def addc(deadbody, Alpha: Aila):
    if len(Alpha.command) == 2:
        id = int(Alpha.text.split(None, 1)[1])
    else:
        id = Alpha.reply_to_message.from_user.id
    u_n = Alpha.reply_to_message.from_user.username
    if u_n:
        lel = u_n
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
    u_n = Alpha.reply_to_message.from_user.username
    if u_n:
        lel = u_n
    else:
        lel = Alpha.reply_to_message.from_user.mention
    if is_sudo(id) is True:
        del_sudo(id)
        await Alpha.reply(f"{lel} is removed as sudo")
    else:
        await Alpha.reply("This user is not a sudo")

@Crystal.on_message(filters.command("crystalsudos") & ~filters.edited & ~filters.forwarded)
async def sudos(_, m: Aila):
    if is_sudo(m.from_user.id) is True:
        sudos = list_all_sudos()
        msg = """"""
        for sudo in sudos:
            mention = (await _.get_users(sudo.i)).mention
            msg += f"\n• {mention} ({sudo.id})\n"
        lol = f"**Crystal Sudos** :- \n\n {msg} \n\n **Count**:- {len(sudos)}"
        await m.reply(lol)

@Crystal.on_message(filters.command("clearall") & filters.user(ALPHA_ID) & ~filters.edited & ~filters.forwarded)
async def clear(_, m: Aila):
    clr_all_sudos()
    await m.reply("All sudos cleared for crystal")
        
