from pyrogram.types import InlineKeyboardButton


class Keshav:
   
    #Alpha Buttons
    alpha_buttons = [
         [InlineKeyboardButton(" Commands ", callback_data="cmda")],
         [InlineKeyboardButton(" Alphaversion ", callback_data="alphaversion")]
    ]


    # Commands
    CMDA = """
**Available commands in Alpha Bot**

/start    - To start the bot ✨💫
/generate - To start string generation !
/help     - To view the tutorial.
/about    - Details to contact the developer !

"""

    # version
    ALPHAVERSION = """
**Alpha Version**

$ Version Name    - end.2.0
$ Version started - 01/05/2022
$ Updated by      - [Alpha](t.me/NotReallyAlpha)

**Updated features**

$ Added "commands" button for new users !
$ Added "Alpha Version" button !
$ Bug fixes 

**Upcoming update**

$ you can see next update on 15/05/2022 !
$ going to add cool pic : when the user starts the bot !

_____
$ If any suggestions  ••>>  [Alpha](t.me/NotReallyAlpha)

"""

    # command buttons
    command_buttons = [
           [InlineKeyboardButton("Click here to Generate", callback_data="generate")],
           [InlineKeyboardButton(text="✨Back🕊", callback_data="home")],
           [InlineKeyboardButton(text="✨Alpha Version💫", callback_data="alphaversion")]
    ]

    # version buttons
    version_buttons = [
           [InlineKeyboardButton("Click here to Generate", callback_data="generate")],
           [InlineKeyboardButton(text="✨Back🕊", callback_data="home")],
           [InlineKeyboardButton(text="✨Commands💫", callback_data="cmda")]
    ]
