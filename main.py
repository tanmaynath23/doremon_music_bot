import os, asyncio, threading, re
from flask import Flask
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pytgcalls import PyTgCalls, filters as TgFilters
from pytgcalls.types import MediaStream
from youtube_search import YoutubeSearch
import yt_dlp

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
STRING_SESSION = os.getenv("STRING_SESSION")

app = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("UserBot", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
call = PyTgCalls(user)

flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return "Bot is Running!"

def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

@app.on_message(filters.command("play") & filters.group)
async def play(_, msg: Message):
    if len(msg.command) < 2:
        return await msg.reply("Gaane ka naam likho! Ex: /play kesariya")
    query = " ".join(msg.command[1:])
    m = await msg.reply(f"🔍 Searching `{query}`...")
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        url = f"https://youtube.com{results[0]['url_suffix']}"
        ydl_opts = {"format": "bestaudio", "quiet": True, "no_warnings": True, "geo_bypass": True, "nocheckcertificate": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']
            title = info.get('title', query)
        await call.play(msg.chat.id, MediaStream(audio_url))
        await m.edit(f"▶️ **Playing:** {title}")
    except Exception as e:
        await m.edit(f"Error: {e}")

async def main():
    threading.Thread(target=run_flask).start()
    await app.start()
    await user.start()
    await call.start()
    print("Music Bot Started!")
    await idle()
    await app.stop()
    await user.stop()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
