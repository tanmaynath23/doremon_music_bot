from pyrogram import Client, filters
from core.call import pytg
from pytgcalls.types import MediaStream
import yt_dlp, os

@Client.on_message(filters.command("play"))
async def play_cmd(c, m):
    if len(m.command) < 2:
        return await m.reply("Gaana likho - /play kesariya")
    query = m.text.split(None,1)[1]
    msg = await m.reply(f"🔍 Searching: {query}")
    try:
        ydl = yt_dlp.YoutubeDL({"format":"bestaudio","quiet":True})
        info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        url = info['url']
        await pytg.play(m.chat.id, MediaStream(url))
        await msg.edit(f"🎧 Playing: {info['title']}\nWelcome to Doremon music Zoox 👋")
    except Exception as e:
        await msg.edit(f"Error: {e}")

@Client.on_message(filters.command("stop"))
async def stop_cmd(c, m):
    await pytg.leave_call(m.chat.id)
    await m.reply("⏹️ Stopped! Doremon music Zoox")
