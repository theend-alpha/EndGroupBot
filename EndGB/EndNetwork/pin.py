from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndDB.sudos_cdb import is_sudo
from EndGB.EndNetwork.sudos import ALPHA_ID

@Crystal.on_message(filters.command(["pin", "unpin"]) & filters.group & ~filters.via_bot & ~filters.edited & ~filters.forwarded)
async def pin(_, m: Aila):
    if m.from_user:
        if m.reply_to_message:
            member = await _.get_chat_member(m.chat.id, m.from_user.id)
            if member.can_pin_messages or m.from_user.id in ALPHA_ID or is_sudo(m.from_user.id):
                if m.command[0][0] == "u":
                    return await m.reply_to_message.unpin()
                await m.reply_to_message.pin()
            else:
                await m.reply(f"you need to be an admin in {m.chat.title} with pin rights")
        else:
            await m.reply("reply to a message to pin")
    else:
        await m.reply("you're using this command with channel or in anonymous mode, try: as user")

                
