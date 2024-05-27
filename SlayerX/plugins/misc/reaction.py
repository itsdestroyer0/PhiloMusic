from pyrogram import filters
from pyrogram.types import Message
import random
from SlayerX import app

emjs = ["😭", "❤️", "🥰", "👏", "🤬", "💋", "🔥", "👍", "🤔", "👀", "😁",]

@app.on_message(filters.chat(-1001548130580) & filters.text)
async def x(_, m: Message):
    await app.send_reaction(-1001548130580, m.id, emoji=random.choice(emjs))
