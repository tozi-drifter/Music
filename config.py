import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME", "DRIFTERSNETWORK")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME", "Drifters_managment_bot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME", "ʏᴜᴍᴇᴋᴏ MUSIC")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME", "Garou_assistant")
EVALOP = list(map(int, getenv("EVALOP", "6392704171").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sanasomani786:TJgADfpkI1XVUkKt@cluster0.ruhyad9.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10000"))

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "18000")
)  # Remember to give value in Minutes

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001929735324"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6392704171"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/tozi-drifter/music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DRIFTERSNETWORK")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DRIFTERS_SUPPORT")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400000")
)  # Remember to give value in Seconds


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "1000"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
# Set this to True if you want the assistant to automatically leave chats after an interval
# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "250"))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Ge@STRINGSEASO_NBOT2 session from @STRINGSEASO_NBOT
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://mallucampaign.in/images/img_1709919340.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://mallucampaign.in/images/img_1709919343.jpg"
)
PLAYLIST_IMG_URL = "https://mallucampaign.in/images/img_1709919344.jpg"
STATS_IMG_URL = "https://mallucampaign.in/images/img_1709919633.jpg"
TELEGRAM_AUDIO_URL = "https://mallucampaign.in/images/img_1709919634.jpg"
TELEGRAM_VIDEO_URL = "https://mallucampaign.in/images/img_1709919637.jpg"
STREAM_IMG_URL = "https://mallucampaign.in/images/img_1709919638.jpg"
SOUNCLOUD_IMG_URL = "https://mallucampaign.in/images/img_1709919639.jpg"
YOUTUBE_IMG_URL = "https://mallucampaign.in/images/img_1709919811.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://mallucampaign.in/images/img_1709919813.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://mallucampaign.in/images/img_1709919880.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://mallucampaign.in/images/img_1709919881.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
