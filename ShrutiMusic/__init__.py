# Copyright (c) 2026 Nitish Sharma <enthemblack>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: enthemblack@gmail.com


from ShrutiMusic.core.bot import Nand
from ShrutiMusic.core.dir import dirr
from ShrutiMusic.core.git import git
from ShrutiMusic.core.userbot import Userbot
from ShrutiMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Nand()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


# ©️ Copyright Reserved - @BlackEnthemOwner

# ==========================================================
# ©️ 2026 Nitish Sharma (enthemblack)
# 🔗 GitHub : https://github.com/enthemblack/EnthemMusicbot
# 📢 Telegram Channel : https://t.me/EnthemMusicSupport
# ==========================================================


# ❤️ Love From 𝓔𝓷𝓽𝓱𝓮𝓶𝓧_𝓜𝓾𝓼𝓲𝓬
