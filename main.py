from flask import Flask
from threading import Thread
import os, asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls, filters as call_filters
from pytgcalls.types import MediaStream
from youtubesearchpython import VideosSearch

# --- Keep Alive for Render ---
app_flask = Flask(__name__)
@app_flask.route('/')
def home(): return "Music Bot Live Hai"
def run_flask():
    app_flask.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
Thread(target=run_flask).start()

# --- Config ---
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
STRING_SESSION = os.getenv("STRING_SESSION")

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("user", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
call = PyTgCalls(user)

@bot.on_message(filters.command("start"))
async def start(_, m):
    await m.reply_text("Bot Live Hai ✅\nGroup me /play song name bhejo!")

@bot.on_message(filters.command("play") & filters.group)
async def play(_, m):
    if len(m.command) < 2:
        return await m.reply("Gaane ka naam likho! Ex: /play Kesariya")
    query = m.text.split(None, 1)[1]
    msg = await m.reply(f"🔍 Searching `{query}`...")
    search = VideosSearch(query, limit=1).result()
    if not search["result"]: return await msg.edit("Nahi mila!")
    link = search["result"][0]["link"]
    title = search["result"][0]["title"]
    await msg.edit(f"▶️ Playing **{title}**")
    try:
        await call.play(m.chat.id, MediaStream(link))
    except Exception as e:
        await msg.edit(f"Error: {e}\nUserbot ko group me add kiya? Voice chat on hai?")

@bot.on_message(filters.command(["stop", "end"]))
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
