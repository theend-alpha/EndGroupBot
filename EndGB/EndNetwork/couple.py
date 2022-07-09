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
        
