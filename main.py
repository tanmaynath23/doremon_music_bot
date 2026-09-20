import os
import pyrogram.errors

# Pytgcalls ke saare missing errors ko dummy bana do
for name in ["GroupcallForbidden", "GroupCallForbidden", "GroupcallInvalid", "GroupCallInvalid", "GroupcallJoinMissing", "GroupCallJoinMissing", "GroupcallNotFound", "GroupCallNotFound", "GroupcallSdpInvalid"]:
    if not hasattr(pyrogram.errors, name):
        setattr(pyrogram.errors, name, type(name, (Exception,), {}))

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
