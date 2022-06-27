from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndNetwork.sudos import ALPHA_ID
from EndGB.EndDB.sudos_cdb import is_sudo

@Crystal.on_message(filters.command("ban") & filters.group & ~filters.edited & ~filters.forwarded & ~filters.via_bot)
async def ban(_, m: Aila):
    if not m.reply_to_message and len(m.command) == 1:
        return await m.reply("Either reply or use /ban < id > to ban")
    me = await _.get_chat_member(m.chat.id, 5507162172)
    if me.can_restrict_members is False:

        return await m.reply("I'm not having sufficient rights to ban users 🤧")
    i_id = m.from_user.id
    if len(m.command) == 2:
        hehe = m.text.split(None, 1)[1]
        if hehe.isnumeric():
            f_id = hehe
        else:
            await m.reply("Try: /ban < user_id >")
    else:
        try:
            f_id = m.reply_to_message.from_user.id
        except:
            await m.reply("replied user is either channel or an anonymous admin")
    try:
        member = await _.get_chat_member(m.chat.id, i_id)
    except:
        pass
    if m.from_user:
        if member.can_restrict_members or i_id in ALPHA_ID or is_sudo(i_id):
            ADMINS = []
            async for user in _.iter_chat_members(m.chat.id, filter="administrators"):
                ADMINS.append(user.user.id)
            if f_id in ADMINS:
                await m.reply("you can't ban an admin 🤧")
            elif is_sudo(f_id):
                await m.reply("you can't ban him 🤧")
            elif f_id in ALPHA_ID:
                await m.reply("Bruhh, he's the owner of this bot 🤧")
            else:
                i_m = (await _.get_users(i_id)).mention
                f_m = (await _.get_users(f_id)).mention
                try:
                    await _.kick_chat_member(m.chat.id, f_id)
                except:
                    pass
                await m.reply(f"{f_m} is banned! And was done by {i_m}")
        else:
            await m.reply(f"you need to be an admin in {m.chat.title} with ban rights to do this 🤧")
    else:
        await m.reply("you're using this command in channel or anonymous admin mode\n\nTry as a user 🤧")


@Crystal.on_message(filters.command("unban") & filters.group & ~filters.edited & ~filters.forwarded & ~filters.via_bot)
async def unban(_, m: Aila):
    if not m.reply_to_message and len(m.command) == 1:
        return await m.reply("Either reply or use /unban < id > to unban")
    me = await _.get_chat_member(m.chat.id, 5507162172)
    if me.can_restrict_members is False:
        return await m.reply("I'm not having sufficient rights to unban users 🤧")
    i_id = m.from_user.id
    if len(m.command) == 2:
        hehe = m.text.split(None, 1)[1]
        if hehe.isnumeric():
            f_id = hehe
        else:
            await m.reply("Try: /unban < user_id >")
    else:
        try:
            f_id = m.reply_to_message.from_user.id
        except:
            await m.reply("replied user is either channel or an anonymous admin")
    try:
        member = await _.get_chat_member(m.chat.id, i_id)
    except:
        pass
    if m.from_user:
        if member.can_restrict_members or is_sudo(i_id) or i_id in ALPHA_ID:
            f_m = (await _.get_users(f_id)).mention
            f_un = (await _.get_users(f_id)).username
            await _.unban_chat_member(m.chat.id, f_id)
            await m.reply(("{} is unbanned!, if banned in {}").format("@" + f_un if f_un else f_m, m.chat.title))
        else:
            await m.reply("you're not an admin to do this")
    else:
        await m.reply("you're using this command in channel or anonymous admin mode\n\nTry as a user 🤧")
            
            
