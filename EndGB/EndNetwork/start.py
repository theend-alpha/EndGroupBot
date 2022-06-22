from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev
from EndGB.EndHelpers import *

@End.on_message(filters.command(["start", "start@EndGroupBot"]) & filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarder)
async def start(maharaj, Dev):
