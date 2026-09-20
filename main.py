import os, threading
from flask import Flask
from core.bot import app
from core.userbot import user
from core.call import pytg
import asyncio
from pyrogram import idle

flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return "Music Bot Pro Running!"

def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.getenv("PORT", 10000)))

async def start_all():
    threading.Thread(target=run_flask, daemon=True).start()
    await app.start()
    await user.start()
    await pytg.start()
    print("Music Bot Pro Started!")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_all())
