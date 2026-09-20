from pyrogram import Client
from pytgcalls import PyTgCalls, idle
import os

API_ID = int(os.environ.get("32223763"))
API_HASH = os.environ.get("74845a85442af570c0d0545c9a223799")
BOT_TOKEN = os.environ.get("8972400222:AAF6a5LfKIjBIA0pTV7qUFOoNk5j6ty")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call = PyTgCalls(app)

@app.on_message()
async def start(client, message):
    await message.reply("Bot Live Hai ✅ - Naya wala chal gaya")

async def main():
    await app.start()
    await call.start()
    print("Bot Started ✅")
    await idle()

import asyncio
asyncio.run(main())
