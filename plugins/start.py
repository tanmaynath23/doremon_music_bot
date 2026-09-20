from pyrogram import Client, filters
@Client.on_message(filters.command("start"))
async def start_cmd(c, m):
    await m.reply_text("Welcome to Doremon music Zoox 👋\n\n🎵 /play gaana - bajane ke liye\n⏹️ /stop - rokne ke liye")
