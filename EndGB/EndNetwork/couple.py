from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.CDB.couples import *
import datetime as dt 

year_month_date = dt.date.today()
y_m_d = str(year_month_date)
year = int(y_m_d[0:4])
month = int(y_m_d[5:7])
date = int(y_m_d[8:])

@Crystal.on_message(filters.command("couples") & ~filters.edited)
async def cpl(_, m):
    if m.chat.type == "private":
        await m.reply("try this command in groups")
    selected = await check_couple(date, month, year)
    if selected:
        lana = await get_couple(date, month, year)
        a = lana["a"]
        b = lana["b"]
        a_m = (await _.get_users(a)).mention
        b_m = (await _.get_users(b)).mention
        csm = f"""Couple of the day has been chosen:
{a_m} + {b_m} = ❤️
[{a}, {b}]

New couple of the day may be chosen at 5 : 30 am next day"""
        await _.send_message(m.chat.id, csm)

    else:
        OMFOO = []
        async for user in _.iter_chat_members(m.chat.id):
            if not user.is_bot:
                OMFOO.append(user.user.id)
        a = random.choice(OMFOO)
        b = random.choice(OMFOO)
        while a == b:
            b = random.choice(OMFOO)
        a_m = (await _.get_users(a)).mention
        b_m = (await _.get_users(b)).mention
        csm = f"""Couple of the day has been chosen:
{a_m} + {b_m} = ❤️
[{a}, {b}]

New couple of the day may be chosen at 5 : 30 am next day"""
        await _.send_message(m.chat.id, csm)
        
