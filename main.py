import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "12345"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

app = Client("alem_music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

@app.on_message(filters.command("start"))
async def start_handler(client, message: Message):
      await message.reply_text("Alem Music Bot is running!")

async def main():
      await app.start()
      await call_py.start()
      print("Bot started successfully!")
      await asyncio.Event().wait()

if __name__ == "__main__":
      asyncio.run(main())
