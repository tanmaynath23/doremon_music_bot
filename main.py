import os
import pyrogram.errors
# Patch for pytgcalls spelling mistake
if not hasattr(pyrogram.errors, "GroupcallForbidden"):
    pyrogram.errors.GroupcallForbidden = pyrogram.errors.GroupCallForbidden

from pyrogram import Client
from pytgcalls import PyTgCalls, idle

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call = PyTgCalls(app)

@app.on_message()
async def start(client, message):
    await message.reply("Bot Live Hai ✅")

async def main():
    await app.start()
    await call.start()
    print("Bot Started ✅")
    await idle()
    await app.stop()

import asyncio
asyncio.run(main())
