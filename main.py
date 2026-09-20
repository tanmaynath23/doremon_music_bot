import os, asyncio, threading
from flask import Flask
from pyrogram import Client, filters, idle
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
import yt_dlp

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
STRING = os.getenv("STRING_SESSION")

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("user", api_id=API_ID, api_hash=API_HASH, session_string=STRING)
call = PyTgCalls(user)

flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return "Bot is Running!"

def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.getenv("PORT", 10000)))

@bot.on_message(filters.command("play") & filters.group)
async def play_func(_, m):
    if len(m.command) < 2:
        return await m.reply("Gaane ka naam likho: /play kesariya")
    q = " ".join(m.command[1:])
    s = await m.reply(f"🔍 Searching `{q}`...")
    try:
        opts = {"format": "bestaudio", "quiet": True, "no_warnings": True, "nocheckcertificate": True, "geo_bypass": True}
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{q}", download=False)['entries'][0]
            link = info['url']
            title = info['title']

        await call.play(m.chat.id, AudioPiped(link))
        await s.edit(f"▶️ Playing: **{title}**")
    except Exception as e:
        await s.edit(f"Error: {e}")

async def main():
    threading.Thread(target=run_flask, daemon=True).start()
    await bot.start()
    await user.start()
    await call.start()
    print("Music Bot Started!")
    await idle()
    await bot.stop()
    await user.stop()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
