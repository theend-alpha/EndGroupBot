from EndGB.CDB import db as rup

couplesdb = rup.couples

async def add_couple(a, b, d, m, y):
    getter = await couplesdb.find_one({"a": a}, {"b": b}, {"d": d}, {"m": m}, {"y": y})
    if getter:
        return
    await couplesdb.insert_one({"a": a}, {"b": b}, {"d": d}, {"m": m}, {"y": y})

