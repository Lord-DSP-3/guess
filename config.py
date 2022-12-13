from json import load
import os
from dotenv import load_dotenv

load_dotenv()

AKI_MONGO_HOST = os.environ.get('aki_mongo_host', "mongodb+srv://gssbotch3:changuess@cluster0.kcyhfzx.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = os.environ.get('bot_token', "5907093089:AAGFgTxZCG52uQo5y4heZ8bxxD8wf9z-WLc")
