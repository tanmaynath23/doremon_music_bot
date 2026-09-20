from flask import Flask
import threading, os
flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return "Doremon Music Zoox is Live!"
threading.Thread(target=lambda: flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))).start()

import asyncio
from core.bot import bot
from core.userbot import user
from core.call import pytg
from pyrogram import idle

async def main():
    await bot.start()
    await user.start()
    await pytg.start()
    print("Welcome to Doremon music Zoox 👋 - Bot Started!")
    await idle()
    await bot.stop()
    await user.stop()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
