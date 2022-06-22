import Config
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="EndGB/EndNetwork"),
)


# Run Bot
if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid,Fooling Alpha or what !")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid,Bot token Bruhh!")
    uname = app.get_me().username
    print(f"@{uname} Started Successfully visit other repositories of Alpha!")
    idle()
    app.stop()
    print("Bot stopped. problem is yours coz this repo made by alpha !")
