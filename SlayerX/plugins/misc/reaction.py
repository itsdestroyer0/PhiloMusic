from pyrogram import filters
from pyrogram.types import Message
import random
from SlayerX import app

emjs = ["😭", "❤️", "🥰", "👏", "🤬", "💋", "🔥", "👍", "🤔", "👀", "😁",]

@app.on_message(filters.chat(message.chat.id) & filters.text)
async def x(_, m: Message):
    await app.send_reaction(m.chat.id, m.id, emoji=random.choice(emjs))
