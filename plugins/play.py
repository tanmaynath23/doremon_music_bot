import yt_dlp
from youtubesearchpython import VideosSearch
from pyrogram import filters
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from core.bot import app
from core.call import pytg

@app.on_message(filters.command("play") & filters.group)
async def play_handler(client, message):
    if len(message.command) < 2:
        return await message.reply("Use: /play kesariya")
    query = " ".join(message.command[1:])
    msg = await message.reply(f"Searching: {query}")
    try:
        search = VideosSearch(query, limit=1).result()
        link = search["result"][0]["link"]
        title = search["result"][0]["title"]
        opts = {"format": "bestaudio", "quiet": True}
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(link, download=False)
            audio_url = info["url"]
        await pytg.play(message.chat.id, AudioPiped(audio_url, HighQualityAudio()))
        await msg.edit(f"Playing: {title}")
    except Exception as e:
        await msg.edit(f"Error: {e}")

@app.on_message(filters.command(["stop","end"]) & filters.group)
async def stop_handler(_, m):
    try:
        await pytg.leave_group_call(m.chat.id)
        await m.reply("Stopped")
    except:
        await m.reply("Nothing playing")
