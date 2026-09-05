# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# Required credentials
API_ID = int(getenv("API_ID", "37844151"))
API_HASH = getenv("API_HASH", "5df278acca1ee0afb87c84e5bb71972b")
BOT_TOKEN = getenv("BOT_TOKEN", "8886382041:AAFkMdsrmpVZOL9WAEFQjpWkdvJ9D2je2yQ")


# Bot and owner info
OWNER_USERNAME = getenv("OWNER_USERNAME", "@sasuke_qt")
BOT_USERNAME = getenv("BOT_USERNAME", "@Mikasax_music_robot")
BOT_NAME = getenv("BOT_NAME", "𝐌ɪᴋᴀsᴀ  ꭙ 𝐌ᴜꜱɪᴄ ♪˼")
ASSUSERNAME = getenv("ASSUSERNAME", "@sasuke_qt")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Sasukeuchihabhai:SASUKEUCHIHA90@cluster0.gv7hurv.mongodb.net/?appName=Cluster0")
 


# Limits and IDs
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", -1003785715622))
OWNER_ID = int(getenv("OWNER_ID", 8672927645))

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
DEEP_API = getenv("DEEP_API")

# Git
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/sasukeuchihaop0987-gif/Alinamusic.git")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ll_ABOUT_SASUKE_ll")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+W3WrSwmHeaY5NjM9")

# Assistant settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

# Song download limits
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# Playlist limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram file limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Session strings
STRING1 = getenv("STRING_SESSION", "BQJBdLcAIpwqX02kFR4lfQNwc_Nfv00cnGYE2G3TUcxE_efvZNO8oK_glyftpMba0k2KRl3_otJZZf6IV7G90VLXiLs_4evham2xSDuZyEhOvinWdq9qgfCtKGjkz_z1nl4KHmKWvgoLoDqyq6PLgMG6w7ObNp-fpZVYWVlCAhx7qGN8FIaR6cWApm8L5qv5FBnZdhnaSoCJyr29mCXJM1Gb3YEWnS862Xre4NxtI5eRssG_iIsgmwrwh1wBY9NdaPUgQzOg33W-ENa3IuruNdMGoI4Qefos5t05TOg2Qgu20kH4LpumwY9jgTs6-1LlqFOLTb4Gt3shFLyqn8QCYvvcxK0UNQAAAAHPl21HAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None) 
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSTION6",None)
STRING7 = getenv("STRING_SESSION7", None)

# Miscellaneous
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

DEBUG_IGNORE_LOG = True

###### IMAGE URLS ######

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/7qj5wo.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/67c3a2.mp4")
PLAYLIST_IMG_URL = "https://files.catbox.moe/lrwbj6.jpg"
STATS_IMG_URL = "https://files.catbox.moe/ybr2ij.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/aesldg.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/aesldg.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/aesldg.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/aesldg.jpg"


SHASHANK_IMG = [
    "https://files.catbox.moe/rjublg.jpg",
    "https://files.catbox.moe/rjublg.jpg",
    "https://files.catbox.moe/rjublg.jpg",
    "https://files.catbox.moe/rjublg.jpg",
    "https://files.catbox.moe/rjublg.jpg",
    "https://files.catbox.moe/rjublg.jpg",
    "https://files.catbox.moe/rjublg.jpg"
]


# Helper function
def time_to_seconds(time: str) -> int:
    """Convert time string (MM:SS) to total seconds."""
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

# Calculate total duration limit in seconds
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validate URLs
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is invalid. It must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is invalid. It must start with https://")
