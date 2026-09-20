from flask import Flask
from threading import Thread
import os

app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot Live Hai"

def run_flask():
    app_flask.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

Thread(target=run_flask).start()
from pyrogram import Client
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message()
async def start(client, message):
    await message.reply("Bot Live Hai ✅ Ab music add karenge")

app.run()
