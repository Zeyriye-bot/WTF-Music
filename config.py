import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Anonymous Music Bot")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "anonymous_was_bot")
ALIVE_NAME = getenv("ALIVE_NAME", "𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦")
BOT_USERNAME = getenv("BOT_USERNAME", "fallen_music_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "fallen_music_here")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DevilsHeavenMF")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DevilsHeavenMF")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/f629901fd6981480e648a.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AnonymousBoy1025/AnonymosMusicBot")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/9a85d0a873e2dd80d278d.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/9e7815284031452afa9e5.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/dcc5e003287f69acea368.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/ed1ce7fee94f46b0f671e.jpg")
