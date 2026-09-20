from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_bot(client, message):
    await message.reply_text(
        "Welcome to Doremon music Zoox 👋\n\n"
        "🎵 Mai tumhara Heavy Music Bot hu!\n"
        "Use /play <gaane ka naam> - VC me bajane ke liye\n"
        "Use /stop - band karne ke liye"
    )
