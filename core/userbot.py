from pyrogram import Client
from config import API_ID, API_HASH, STRING_SESSION
user = Client("user", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
