# (c) 

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", ))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001654604022))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/anumitultrabots'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/anumitultrabots'>anumitultrabots</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/ajak4405'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @anumitultrabots</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @anumitultrabots</a></b>
"""


