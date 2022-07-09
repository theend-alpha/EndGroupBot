from EndGB.CDB import db as rup

couplesdb = rup.couples

async def add_couple(a, b, d, m, y):
    getter = await couplesdb.find_one({"a": a}, {"b": b}, {"d": d}, {"m": m}, {"y": y})
    if getter:
        return
    await couplesdb.insert_one({"a": a}, {"b": b}, {"d": d}, {"m": m}, {"y": y})

async def check_couple(d, m, y):
    getter = await couplesdb.find_one({"d": d}, {"m": m}, {"y": y}, {"a": {$gt: 0}}, {"b": {$gt: 0}})
    if getter:
        return True
    else:
        return False

async def get_couple(d, m, y):
    getter = await couplesdb.find_one({"d": d}, {"m": m}, {"y": y}, {"a": {$gt: 0}}, {"b": {$gt: 0}})
    try:
        return getter
    except:
        pass
    
