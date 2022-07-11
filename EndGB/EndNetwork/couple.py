from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.CDB.couples import *
import datetime as dt 
import random

year_month_date = dt.date.today()
y_m_d = str(year_month_date)
year = int(y_m_d[0:4])
month = int(y_m_d[5:7])
date = int(y_m_d[8:])

@Crystal.on_message(filters.command("couples") & ~filters.edited)
async def cpl(_, m):
    if m.chat.type == "private":
        await m.reply("try this command in groups")
    couples = await get_couples()
    for couple in couples:
        lel = couple.split()
        if lel[2] == date and lel[3] == month and lel[4] == year:
            c1 = int(lel[0])
            c2 = int(lel[1])
            c1_m = (await _.get_users(c1)).mention
            c2_m = (await _.get_users(c2)).mention
            csm = f"""Couple of the day:\n\n
{c1_m} + {c2_m} = ❤️\n\n
New couple of the day may be chosen at 5 : 30 am next day!"""
            ok = await _.send_message(m.chat.id, csm)
        
        if ok:
            return
        else:
            KIDS = []
            async for user in _.iter_chat_members(m.chat.id)
                if user.user.is_bot:
                    return
                KIDS.append(user.user.id)
            if len(KIDS) < 2:
                await m.reply("Not enough users to ship ")
            c1 = random.choice(KIDS)
            c2 = random.choice(KIDS)
            while c1 == c2:
                c2 = random.choice(KIDS)
            c1_m = (await _.get_users(c1)).mention
            c2_m = (await _.get_users(c2)).mention
            csm = f"""Couple of the day:\n\n
{c1_m} + {c2_m} = ❤️\n\n
New couple of the day may be chosen at 5 : 30 am next day!"""
            lel = f"{c1} {c2} {date} {month} {year}"
            await add_couple(lel)
            await _.send_message(m.chat.id, csm)


     
