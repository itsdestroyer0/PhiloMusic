from pyrogram import filters
from pyrogram.types import Message
import random
from SlayerX import app

emjs = ["😭", "❤️", "🥰", "👏", "🤬", "💋", "🔥", "👍", "🤔", "👀", "😁",]

chat_id = message.chat.id

@app.on_message(filters.chat(chat_id) & filters.text)
async def x(_, m: Message):
    await app.send_reaction(m.chat.id, m.id, emoji=random.choice(emjs))
