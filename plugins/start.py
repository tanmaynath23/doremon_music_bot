from pyrogram import filters
from core.bot import app
@app.on_message(filters.command("start"))
async def start(_, m):
    await m.reply(f"Hello {m.from_user.mention}! Pro Music Bot Ready. Use /play in groups.")
