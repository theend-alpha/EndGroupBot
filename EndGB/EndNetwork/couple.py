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
