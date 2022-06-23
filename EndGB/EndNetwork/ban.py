from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev

BAN_TEXT = "{} is banned by {} !"

@End.on_message(filters.command("ban") & filters.group & ~filters.forwarded & ~filters.edited & ~filters.via_bot)
async def ban(alpha, keshav: Dev):
    admins = await alpha.get_chat_administrators(keshav.chat.id)
    ADMINS = []
    BANNERS = []
    for admin in admins:
        id = admin["user"]["id"]
        ADMINS.append(id)
    for admin in admins:
        if admin["can_restrict_members"]:
            BANNERS.append(admin["user"]["id"])
    if keshav.from_user.id in ADMINS:
        if keshav.from_user.id in BANNERS:
            await alpha.kick_chat_member(keshav.chat.id, keshav.reply_to_message.from_user.id)
            await alpha.send_message(keshav.chat.id, BAN_TEXT.format(keshav.reply_to_message.from_user.mention, keshav.from_user.mention))
        else:
            await keshav.reply("you don't having ban rights to ban or restrict users !")
    else:
        await keshav.reply("You're not an admin to do this !")

    ADMINS.clear()
    BANNERS.clear()
