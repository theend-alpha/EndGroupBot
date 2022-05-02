from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}!! Nice to see ya here !

Welcome to {} Made by Alpha © 

End Version - end.2.0 ©

Last updated - 01/05/2022

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Click here to Generate", callback_data="generate")],
        [InlineKeyboardButton(text=" Back ", callback_data="home")],
        [InlinekeyboardButton(text=" Commands ", callback_data="commands")]
    ]

    generate_button = [
        [InlineKeyboardButton("Click here to Generate", callback_data="generate")]
    ]

    support_button = [
        [InlineKeyboardButton("Group", url="https://t.me/BTS_CHAT_ZONE")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Click here to Generate", callback_data="generate")],
        [
            InlineKeyboardButton("Tutorial", callback_data="help"),
            InlineKeyboardButton("Contact", callback_data="about")
        ],
        [
            InlineKeyboardButton("Owner", url="https://t.me/NotReallyAlpha"),
            InlineKeyboardButton("Group", url="https://t.me/BTS_CHAT_ZONE")
        ],
        [
            InlineKeyboardButton("Commands", callback_data="commands"),
            InlineKeyboardButton("Alpha Version", callback_data="alphaversion")
        ],
    ]

    # Help Message
    HELP = """

» click on generate button ; Then you'll get to see two buttons 
» 1.Pyrogram - For music bots 
» 2.Telethon - For all bots except music one !
» Choose what ya want ! 
» Submit API ID , API HASH , NUMBER , CODE !
» STRING WILL BE SENT TO SAVED MESSAGES ! ✨💫
____

Thx for using our bot ! ✨💫

"""

    # About Message
    ABOUT = """
** Alpha String Bot © **

Bot to generate session with privacy ! [©](https://t.me/NotReallyAlpha) 

[𝐃𝐄𝐯𝐄𝐬𝐇](https://t.me/iTz_DEv_xD) | [𝐀𝐋𝐏𝐇𝐀](https://t.me/NotReallyAlpha)

Language Used : Python
           
Contact Owner and Developers [here](https://t.me/BTS_CHAT_ZONE) 
"""
