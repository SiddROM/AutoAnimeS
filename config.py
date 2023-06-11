import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv('config.env')
elif os.path.exists("sample.env"):
    load_dotenv("sample.env")

API_ID = os.getenv("26019444")
API_HASH = os.getenv("a308fac723905cdbd836414b18f3b3d6")
BOT_TOKEN = os.getenv("6100344970:AAGrq-OnnEwz9KBahxtCcdo68pXG7kV6Z1I")
MONGO_DB_URI = os.getenv("mongodb+srv://xenfilebot:xenfilebot@cluster0.sskycsa.mongodb.net/?retryWrites=true&w=majority")
STATUS_MSG_ID = os.getenv("573")
SCHEDULE_MSG_ID = os.getenv("574")
CHANNEL_TITLE = os.getenv("CHANNEL_TITLE", "REALM OF WEEBS")
INDEX_CHANNEL_USERNAME = os.getenv("OngoingAnimeIndex")
UPLOADS_CHANNEL_USERNAME = os.getenv("OngoingAnimeRealms")
TECHZ_API_KEY = os.getenv("GUUOXT")
COMMENTS_GROUP_LINK = os.getenv("https://t.me/+KUxfqDGbQj0zMTM1")
SLEEP_TIME = os.getenv("15", 60)

for k, v in {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "MONGO_DB_URI": MONGO_DB_URI,
    "STATUS_MSG_ID": STATUS_MSG_ID,
    "SCHEDULE_MSG_ID": SCHEDULE_MSG_ID,
    "INDEX_CHANNEL_USERNAME": INDEX_CHANNEL_USERNAME,
    "UPLOADS_CHANNEL_USERNAME": UPLOADS_CHANNEL_USERNAME,
    "TECHZ_API_KEY": TECHZ_API_KEY,
    "COMMENTS_GROUP_LINK": COMMENTS_GROUP_LINK,
}.items():
    if not v:
        raise Exception(f"{k} not found .env file, please add it to use AutoAnimeBot")
