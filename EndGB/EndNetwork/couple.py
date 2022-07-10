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
    couples = await get_couples()
    for couple in couples:
        lel = couple.split()
        if lel[2] == date and lel[3] == month and lel[4] == year:
            c1 = int(lel[0])
            c2 = int(lel[1])
