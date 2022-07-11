from EndGB.CDB import db as rup

couplesdb = rup.couples

async def add_couple(a: str):
    await couplesdb.insert_one({"a": a})

async def get_couples():
    lel = couplesdb.find({"a": {"$gt": 0}})
    if not lel:
        return []
    OMFOO = []
    for user in await lel.to_list(length=1000000000):
        OMFOO.append(user)
    return OMFOO
