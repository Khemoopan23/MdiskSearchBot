# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 17737898))
    API_HASH = os.environ.get("API_HASH", "ad762fe0516f367115ba651d929cf429")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5657801755:AAFASLmkl6diuREYdpPfAHVIh9Swkoc8Dsw")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQCoADjfDF5RqE0rEiSQFyqGaKoTpxLv-Sdm2a-gq-PV7YS--hN3PmBvgTo88qwuCJxjxfDV7oW6DMW9ti4qED_-Lso9X-WhdwPi3MAEQ4MjG1e2ZwKOXYgiTefUQ77asGDQkYSvEKKrgerR_2PE1jhft0Rt6uc4PskQqkxEEAmUgclcvZOhg2-Lg_FHm3YmfSlo_n_LC-SAx8ERuv54kSWLZQbgXjnVIgjXurXpZYIF4a-Dx8PXeCxYc9uOtMHKfomMM5Qt78aJp5DL6Rvqy0_wMj4DfI2m32HjZMT1v-p1TJnCR4OnUiZtqTvQvvb264X9Tq3ER6O-w8d8-uBnRMMsAAAAAUKBF3YA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001654604022))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MdiskSearchv1bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5076949930"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001666254490")
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


