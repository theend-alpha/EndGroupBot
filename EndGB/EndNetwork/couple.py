from pyrogram import Client as Crystal, filters
from pyrogram.types import Message as Aila
from EndGB.EndDB.couples_cdb import *
import datetime as dt 

year_month_date = dt.date.today()
y_m_d = str(year_month_date)
year = int(y_m_d[0:4])
month = int(y_m_d[5:7])
date = int(y_m_d[8:])

@Crystal.on_message(filters.command(["couple", "couples", "shipping", "shipping@EndCrystalBot"]) & ~filters.edited & ~filters.via_bot)
async def couple(_, m: Aila):
    if m.chat.type == "private":
        return await m.reply("try this command in groups")
    if m.from_user:
        if couple_found(date, month, year):
            COUPLE = []
            couples = get_couples()
            for couple in couples:
                COUPLE.append(couple.c1_id)
                COUPLE.append(couple.c2_id)
            c1_id = COUPLE[0]
            c2_id = COUPLE[1]
            c1_m = (await _.get_users(c1_id)).mention
            c2_m = (await _.get_users(c2_id)).mention
            c_s_m = f"""Couple of the day has been chosen:
{c1_m} + {c2_m} = ❤️
[{c1_id}, {c2_id}]

New couple of the day may be chosen at 5:30 am"""

            await _.send_message(m.chat.id, c_s_m)
        else:
            ALL = []
            async for user in _.iter_chat_members(m.chat.id):
                if user.user.is_bot:
                    pass
                elif user.user.is_deleted:
                    pass
                else:
                    ALL.append(user.user.id)
            if len(ALL) < 2:
                return await m.reply("no enough users to ship 🤧")
            c1_id = random.choice(ALL)
            c2_id = random.choice(ALL)
            while c1_id == c2_id:
                c2_id = random.choice(ALL)
            c1_m = (await _.get_users(c1_id)).mention
            c2_m = (await _.get_users(c2_id)).mention
            c_s_m = f"""Couple of the day has been chosen:
{c1_m} + {c2_m} = ❤️
[{c1_id}, {c2_id}]

New couple of the day may be chosen at 5:30 am"""

            couple_of_the_day(c1_id, c2_id, date, month, year)
            couple_selected_today(date, month, year)
            await _.send_message(m.chat.id, c_s_m)
    
