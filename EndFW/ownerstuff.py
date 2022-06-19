from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev
from EndFW.AlphaDatabase.users_db import *

@End.on_message(filters.command("users") & filters.user(ALPHA_ID) & ~filters.edited & ~filters.forwarded)
async def users(Alpha, Doli: Dev):
    users = get_users()
    pusers = get_pusers()
    USERS = []
    PUSERS = []
    for user in users:
        USERS.append(user.id)
    for puser in pusers:
        PUSERS.append(puser.id)
    no_users = len(USERS)
    no_pusers = len(PUSERS)
    await Doli.reply(f"*Total Users* \n\n • Count :- {no_users} \n\n*Private Users* \n\n • Count :- {no_pusers}")
