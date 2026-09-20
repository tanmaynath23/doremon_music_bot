from flask import Flask
from threading import Thread
import os, asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
from youtubesearchpython import VideosSearch

app_flask = Flask(__name__)
@app_flask.route('/')
def home(): return "Music Bot Live Hai"
def run_flask():
    app_flask.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
Thread(target=run_flask).start()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
STRING_SESSION = os.getenv("STRING_SESSION")

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("user", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
call = PyTgCalls(user)

@bot.on_message(filters.command("start"))
async def start(_, m):
    await m.reply_text("Bot Live Hai ✅")

@bot.on_message(filters.command("play") & filters.group)
async def play(_, m):
    if len(m.command) < 2:
        return await m.reply("Naam likho - /play kesariya")
    query = m.text.split(None, 1)[1]
    msg = await m.reply(f"🔍 Searching `{query}`...")
    res = VideosSearch(query, limit=1).result()
    if not res["result"]: return await msg.edit("Nahi mila!")
    link = res["result"][0]["link"]
    title = res["result"][0]["title"]
    await msg.edit(f"▶️ Playing **{title}**")
    try:
        await call.play(m.chat.id, MediaStream(link))
    except Exception as e:
        await msg.edit(f"Error: {e}")

@bot.on_message(filters.command(["stop"]))
async def stop(_, m):
    await call.leave_call(m.chat.id)
    await m.reply("⏹️ Stopped!")

async def main():
    await user.start()
    await bot.start()
    await call.start()
    print("Music Bot Started!")
    await asyncio.Event().wait()

asyncio.run(main())
